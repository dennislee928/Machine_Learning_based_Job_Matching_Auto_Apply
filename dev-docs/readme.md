✅ 步驟一：擴充職缺資料來源，進行相似度推薦（ranker.py 搭配）

你需要模擬或建立一些「職缺描述」→ 轉成向量 → 與你的履歷向量做比較：
➤ 任務：

    建立 jobs.json（5~10 筆職缺）

    增加 vectorizer.py 中 generate_job_vectors() function

    使用 ranker.py 比對推薦順序

我可以幫你生出這批 mock 職缺，並加到 backend-py/data/jobs.json。
✅ 步驟二：開始開發 golang-fetcher/ 的 fetchers

讓 Go 幫你把這些雲端作品資料拉進來（之後可供 Python 使用）：
平台 目標 建議技術
GitHub 使用 REST API 抓 pinned repos, language stats net/http, encoding/json
R2 / Netlify / Vercel public 頁面掃描 + metadata goquery, http.Get
Snyk 用 REST API 抓到你最近掃描的 repo 報告 http.Client, Bearer token

你也可以叫我幫你生成 github.go（client），支援 .env token 載入與資料結構解析。
✅ 步驟三（部署）：測試 + 上線
模組 部署平台 說明
backend-py Render（可先跑 CLI） 實作 FastAPI 或維持 CLI
golang-fetcher Fly.io 實作 GET /resume-data API，提供 Resume 資料供 backend 拉用
Cloud Resume / Letter 展示頁 Cloudflare Pages + GitHub Actions 選擇性上傳 markdown 轉 HTML 展示頁面
💡 建議的優先順序

    🧪 先讓 Python 端完成：履歷向量 + 模擬職缺向量 + 相似度排序

    🧩 再讓 Golang 拉 cloud profiles，接給 Python 串接

    🚀 若有時間再部署上線（可保留本機測試為第一版）
