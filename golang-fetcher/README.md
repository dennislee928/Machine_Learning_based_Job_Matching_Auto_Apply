# 職缺抓取 API 服務

這是用於 Job Matcher 專案的 Golang 抓取服務，負責連接 104 和 CakeResume 等平台，抓取職缺信息並提供 API 接口。

## 功能特點

- 支援從 104 人力銀行抓取職缺
- 支援從 CakeResume 平台抓取職缺
- 提供統一的 REST API 用於職缺搜索和投遞
- 整合自動應徵功能

## 環境需求

- Go 1.19 或以上
- 具備 CakeResume API Token (如需使用 CakeResume 相關功能)

## 安裝與運行

1. 複製 `.env.example` 為 `.env` 並填入必要的設定：

```bash
cp .env.example .env
```

2. 編輯 `.env` 設定您的 API 密鑰和其他配置。

3. 安裝依賴：

```bash
go mod download
```

4. 運行服務：

```bash
go run main.go
```

服務將在 http://localhost:8080 (或您指定的端口) 運行。

## API 接口

### 獲取 104 職缺

```
GET /api/104/jobs?keyword=golang
```

### 獲取 CakeResume 職缺

```
GET /api/cakeresume/jobs?keyword=golang
```

### 提交職缺應徵

```
POST /api/apply
```

請求體:

```json
{
  "job_id": "12345",
  "source": "104", // 或 "cakeresume"
  "resume_text": "您的履歷內容",
  "cover_letter": "您的求職信內容"
}
```

## 擴展

要支援更多的職缺平台，請在 `client` 包中實現 `JobClient` 接口：

```go
type JobClient interface {
    FetchJobs(keyword string, limit int) ([]JobPost, error)
    ApplyJob(jobID string, resumeText string, coverLetter string) error
}
```
