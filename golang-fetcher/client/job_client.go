package client

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"time"
)

// JobPost 結構體用於存儲職缺資訊
type JobPost struct {
	ID          string `json:"id"`
	Title       string `json:"title"`
	Company     string `json:"company"`
	Description string `json:"description"`
	URL         string `json:"url"`
	Source      string `json:"source"` // "104" 或 "cakeresume"
	PostedDate  string `json:"posted_date,omitempty"`
}

// JobClient 介面定義職缺抓取的方法
type JobClient interface {
	// FetchJobs 抓取職缺並返回結構化的職缺清單
	FetchJobs(keyword string, limit int) ([]JobPost, error)
	// ApplyJob 應用於特定職缺
	ApplyJob(jobID string, resumeText string, coverLetter string) error
}

// OneOFourClient 實現 104 網站的職缺抓取
type OneOFourClient struct {
	BaseURL    string
	HTTPClient *http.Client
}

// CakeResumeClient 實現 CakeResume 網站的職缺抓取
type CakeResumeClient struct {
	BaseURL    string
	APIToken   string
	HTTPClient *http.Client
}

// 創建新的 104 客戶端
func NewOneOFourClient() *OneOFourClient {
	return &OneOFourClient{
		BaseURL: "https://www.104.com.tw/jobs/search/list",
		HTTPClient: &http.Client{
			Timeout: time.Second * 10,
		},
	}
}

// 創建新的 CakeResume 客戶端
func NewCakeResumeClient(apiToken string) *CakeResumeClient {
	return &CakeResumeClient{
		BaseURL:  "https://api.cakeresume.com/v1",
		APIToken: apiToken,
		HTTPClient: &http.Client{
			Timeout: time.Second * 10,
		},
	}
}

// FetchJobs 實現 104 職缺抓取邏輯
func (c *OneOFourClient) FetchJobs(keyword string, limit int) ([]JobPost, error) {
	// 這裡只是一個範例實現，實際上需要更複雜的抓取和解析邏輯
	// 可能需要模擬瀏覽器行為或使用第三方庫進行 HTML 解析
	url := fmt.Sprintf("%s?keyword=%s&mode=s&jobsource=2018indexpoc", c.BaseURL, keyword)
	
	// 實作後續的 HTTP 請求和解析邏輯
	// ...

	// 返回模擬數據作為示例
	mockJobs := []JobPost{
		{
			ID:          "12345",
			Title:       "後端工程師",
			Company:     "範例科技公司",
			Description: "熟悉 Golang, Python 等後端技術",
			URL:         "https://www.104.com.tw/job/12345",
			Source:      "104",
			PostedDate:  "2023-04-15",
		},
	}
	
	return mockJobs, nil
}

// ApplyJob 實現 104 職缺應徵邏輯
func (c *OneOFourClient) ApplyJob(jobID string, resumeText string, coverLetter string) error {
	// 實現職缺應徵邏輯
	// 這需要模擬表單提交或使用 104 的 API（如果有的話）
	
	fmt.Printf("模擬應徵 104 職缺 ID %s\n", jobID)
	return nil
}

// FetchJobs 實現 CakeResume 職缺抓取邏輯
func (c *CakeResumeClient) FetchJobs(keyword string, limit int) ([]JobPost, error) {
	url := fmt.Sprintf("%s/search/jobs?q=%s&limit=%d", c.BaseURL, keyword, limit)
	
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return nil, err
	}
	
	req.Header.Add("Authorization", fmt.Sprintf("Bearer %s", c.APIToken))
	req.Header.Add("Content-Type", "application/json")
	
	resp, err := c.HTTPClient.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()
	
	// 解析回應
	// 實際實現需要根據 CakeResume API 的回應格式調整
	// ...
	
	// 返回模擬數據
	mockJobs := []JobPost{
		{
			ID:          "cake-12345",
			Title:       "前端工程師",
			Company:     "CakeResume 科技",
			Description: "熟悉 React, Vue 等前端框架",
			URL:         "https://www.cakeresume.com/jobs/cake-12345",
			Source:      "cakeresume",
			PostedDate:  "2023-04-10",
		},
	}
	
	return mockJobs, nil
}

// ApplyJob 實現 CakeResume 職缺應徵邏輯
func (c *CakeResumeClient) ApplyJob(jobID string, resumeText string, coverLetter string) error {
	url := fmt.Sprintf("%s/jobs/%s/apply", c.BaseURL, jobID)
	
	payload := map[string]string{
		"resume": resumeText,
		"cover_letter": coverLetter,
	}
	
	jsonPayload, err := json.Marshal(payload)
	if err != nil {
		return err
	}
	
	req, err := http.NewRequest("POST", url, bytes.NewBuffer(jsonPayload))
	if err != nil {
		return err
	}
	
	req.Header.Add("Authorization", fmt.Sprintf("Bearer %s", c.APIToken))
	req.Header.Add("Content-Type", "application/json")
	
	resp, err := c.HTTPClient.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	
	if resp.StatusCode != http.StatusOK && resp.StatusCode != http.StatusCreated {
		body, _ := ioutil.ReadAll(resp.Body)
		return fmt.Errorf("應徵失敗: %s, 狀態碼: %d", string(body), resp.StatusCode)
	}
	
	return nil
} 