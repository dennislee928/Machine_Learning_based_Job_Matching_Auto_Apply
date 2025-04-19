package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/joho/godotenv"
	"github.com/lipeichen/job-matcher/client"
)

type AppConfig struct {
	CakeResumeAPIToken string
	Port               string
}

func loadConfig() (AppConfig, error) {
	err := godotenv.Load()
	if err != nil {
		log.Println("警告: 無法載入 .env 檔案")
	}

	config := AppConfig{
		CakeResumeAPIToken: os.Getenv("CAKERESUME_API_TOKEN"),
		Port:               os.Getenv("PORT"),
	}

	if config.Port == "" {
		config.Port = "8080" // 默認端口
	}

	return config, nil
}

func main() {
	config, err := loadConfig()
	if err != nil {
		log.Fatalf("無法載入配置: %v", err)
	}

	// 初始化客戶端
	oneOFourClient := client.NewOneOFourClient()
	cakeResumeClient := client.NewCakeResumeClient(config.CakeResumeAPIToken)

	// API 路由
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("職缺抓取服務正在運行"))
	})

	// 104 職缺API
	http.HandleFunc("/api/104/jobs", func(w http.ResponseWriter, r *http.Request) {
		keyword := r.URL.Query().Get("keyword")
		if keyword == "" {
			http.Error(w, "請提供搜尋關鍵字", http.StatusBadRequest)
			return
		}

		jobs, err := oneOFourClient.FetchJobs(keyword, 10)
		if err != nil {
			http.Error(w, fmt.Sprintf("抓取職缺失敗: %v", err), http.StatusInternalServerError)
			return
		}

		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(jobs)
	})

	// CakeResume 職缺API
	http.HandleFunc("/api/cakeresume/jobs", func(w http.ResponseWriter, r *http.Request) {
		keyword := r.URL.Query().Get("keyword")
		if keyword == "" {
			http.Error(w, "請提供搜尋關鍵字", http.StatusBadRequest)
			return
		}

		jobs, err := cakeResumeClient.FetchJobs(keyword, 10)
		if err != nil {
			http.Error(w, fmt.Sprintf("抓取職缺失敗: %v", err), http.StatusInternalServerError)
			return
		}

		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(jobs)
	})

	// 職缺應徵API
	http.HandleFunc("/api/apply", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			http.Error(w, "僅支持 POST 請求", http.StatusMethodNotAllowed)
			return
		}

		var request struct {
			JobID       string `json:"job_id"`
			Source      string `json:"source"` // "104" 或 "cakeresume"
			ResumeText  string `json:"resume_text"`
			CoverLetter string `json:"cover_letter"`
		}

		if err := json.NewDecoder(r.Body).Decode(&request); err != nil {
			http.Error(w, "無效的請求格式", http.StatusBadRequest)
			return
		}

		var applyErr error
		switch request.Source {
		case "104":
			applyErr = oneOFourClient.ApplyJob(request.JobID, request.ResumeText, request.CoverLetter)
		case "cakeresume":
			applyErr = cakeResumeClient.ApplyJob(request.JobID, request.ResumeText, request.CoverLetter)
		default:
			http.Error(w, "不支持的職缺來源", http.StatusBadRequest)
			return
		}

		if applyErr != nil {
			http.Error(w, fmt.Sprintf("應徵失敗: %v", applyErr), http.StatusInternalServerError)
			return
		}

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(map[string]string{"status": "success", "message": "應徵成功"})
	})

	// 啟動服務器
	port := fmt.Sprintf(":%s", config.Port)
	log.Printf("服務啟動於 http://localhost%s", port)
	log.Fatal(http.ListenAndServe(port, nil))
}