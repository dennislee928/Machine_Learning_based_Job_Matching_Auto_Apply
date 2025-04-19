# Job Matcher AI

An automated job recommendation and application system based on Natural Language Processing (NLP) and semantic vector comparison. It supports GitHub/R2 resume parsing and integrates with platforms like 104 and CakeResume to generate customized cover letters and automate job applications.

---

## 🚀 Features

- NLP-based skill extraction and semantic vector generation (supports Chinese).
- Job vacancy crawling and JSON structured analysis (Python crawler).
- Vector comparison for job recommendation (FAISS / Sentence-BERT).
- ChatGPT-powered automatic cover letter and resume summary generation.
- Golang API integration for platform application behavior (supports .env).
- Cross-platform modular architecture for easy expansion to other job sources.
- Integration with free Microsoft Cloud Partner (MCP) resources (Power Automate, Azure AI).

---

## 🧮 Architecture

```mermaid
graph TD
  subgraph Python (AI Layer)
    A[GitHub Resume Analysis] --> B[NLP Skill Vector Extraction]
    B --> C[Job Vector Comparison]
    C --> D[ChatGPT Cover Letter Generation]
    D -->|REST Request| E[Golang API Application Submission]
  end

  subgraph Golang (Platform Integration)
    E --> F[Connect CakeResume API]
    E --> G[Simulate 104 Form Filling]
  end
```

---

## 🛠️ Tech Stack

| Layer         | Technology                                    | Purpose                                     |
| :------------ | :-------------------------------------------- | :------------------------------------------ |
| AI Model      | Python / transformers / sentence-transformers | Semantic extraction and vector generation   |
| Vector Search | FAISS / LlamaIndex                            | Job and resume comparison                   |
| Chat Model    | OpenAI GPT-4                                  | Generate cover letters and resume summaries |
| Platform      | Golang                                        | API fetching, application submission        |
| Automation    | n8n, Power Automate                           | Notifications, form workflows               |
| MCP Support   | Azure OpenAI, Logic Apps                      | Build No-Code workflows                     |
| Security      | .env                                          | Separate API keys and account secrets       |

---

## ⚙️ Usage

1.  Create a `.env` file with the following variables:

    ```
    OPENAI_API_KEY=your_openai_key
    CAKERESUME_API_TOKEN=your_token
    GITHUB_USERNAME=your_github_id
    ```

2.  Install Python dependencies:

    ```
    pip install -r requirements.txt
    ```

3.  Run the main process (recommendation + cover letter):

    ```
    python main.py
    ```

4.  Start the Golang module for application submission (in a separate terminal):

    ```
    cd golang-fetcher
    go run main.go
    ```

---

## 🎯 Roadmap

Refer to `docs/implementation_plan.md` for the project timeline and goals.

Example:

| Stage              | Task                                          | Date             |
| :----------------- | :-------------------------------------------- | :--------------- |
| NLP Architecture   | SBERT modeling and skill extraction           | 2025/04/20-24    |
| Job Crawling       | 104 / CakeResume automatic scraping           | 2025/04/25-28    |
| Golang API         | REST receive application requests and forward | 2025/04/29-05/03 |
| Testing + Optimize | Automatic output + batch application process  | 2025/05/04-08    |

---

## ➡️ Future Directions

- ✅ Add LinkedIn / Yourator job source modules (Golang client).
- ✅ Implement FastAPI + Vue frontend/backend separation Dashboard.
- ✅ Adopt Azure OpenAI Chat Completion for commercial deployment (via MCP free plan).
- ✅ Implement simple CI/CD: GitHub Actions automatically package resume analysis + push recommendation reports.
- ✅ AI Resume Review: Combine Scoring model to determine the match score between each JD and your resume.

---

✅ 全免費部署策略（個人使用 + 可展示）
模組 建議平台 優勢 免費條件 / 限制
backend/ (Python NLP + GPT) Render Free Web Service 支援 Python Web App，自動部署 CI/CD 每月 750 小時，5 分鐘休眠限制
golang-fetcher/ (應徵 API) Fly.io Free VM 可部署 Golang REST API，支援 global VM 每月 3,000 VM-min + 3GB volume
.env 機密管理 Render/Fly.io Secrets 原生支援 .env 設定與機密保管 無需額外費用
自動化投遞 + 通知 n8n Free Cloud 免費 workflow builder，可串 webhook/Google Sheets 每月 200 workflow 執行
Resume 可視化頁面 Cloudflare Pages 靜態網頁展示推薦職缺、履歷摘要 無限佈署、免費流量、支援 GitHub Actions
儲存個人推薦資料 GitHub + Pages 或 Supabase Free DB Git 儲存 Markdown 檔案、自動產出報告 Supabase 有 500MB Free Tier DB
💡 Microsoft Cloud Partner（MCP）Bonus 加值應用（也都是免費！）
工具 用途 說明 / 優勢
Azure OpenAI GPT 生成 Cover Letter 通常有 5~10 萬 token 免費試用額度（可請專案帳號）
Power Automate 將履歷分析結果推送至 Teams、Email、Line Notify 設定簡單、不用寫程式
Power BI Embedded 可視化職缺推薦分數 上傳分析表格，自動產生圖表
Azure Logic Apps 串接外部 webhook → Google Sheet 類似 Zapier，可與 Python REST API 配合
📦 範例整合架構（免費版全流程）

graph TD
A[GitHub/R2 履歷] --> B(Python NLP 後端 - Render)
B --> C{相似度計算 + Cover Letter}
C --> D[Golang API 投遞 - Fly.io]
D --> E[職缺平台（104 / Cake）]

B --> F[Cloudflare Pages 靜態展示]
D --> G[Azure Power Automate 通知你成功/失敗]

🚀 下一步建議
你想要... 我可以幫你做的事
自動部署 Python 到 Render 幫你生成 render.yaml + FastAPI backend
快速部署 Golang 到 Fly.io 幫你做 fly.toml + build script
MCP 工作流自動化 幫你接 webhook → Power Automate → 你的信箱/Line
打包推薦職缺頁面 幫你用 Next.js 或 Astro + GitHub Actions 部署 Cloudflare Pages

---

✅ 要補完的內容整理
🔧 backend-py/ 應具備的模組（Python）
檔案 功能說明
main.py 主入口，觸發履歷向量生成 + 呼叫 GPT 產生 Cover Letter
resume_parser.py 擷取 GitHub/R2/Snyk/Vercel 等來源的履歷內容與專案摘要
vectorizer.py 使用 Sentence-BERT 轉換成語意向量
ranker.py 與職缺向量比對，相似度排序推薦
letter_generator.py 用 OpenAI API 生成自我推薦信
utils/env_loader.py .env 載入（使用 dotenv）
docs/implementation_plan.md 原本就有的實行計畫書
🚀 golang-fetcher/ 功能擴充目標

    讀取 .env 拿取你的 GitHub / R2 / Netlify 等 token 或公開頁面

    建立 fetch client 抓取以下資料：

        GitHub：README、Pinned Repos、Languages

        R2 / Vercel / Netlify：個人展示作品集網址

        Snyk：安全掃描報告頁（可作為資安能力證明）

🌱 建議的 .env 結構

# OpenAI / GPT 用

OPENAI_API_KEY=...

# GitHub

GITHUB_USERNAME=dennislee928
GITHUB_TOKEN=...

# R2 / Vercel / Netlify 公開頁

PORTFOLIO_R2_URL=https://r2.dev/...
PORTFOLIO_VERCEL=https://xxx.vercel.app
PORTFOLIO_NETLIFY=https://xxx.netlify.app

# Snyk 安全報告（可公開 link）

SNYK_PROJECT_URL=https://app.snyk.io/org/...

🧩 我可以幫你產出這些：

    backend-py/ 全部需要的 Python 檔案（含 .env 支援）

    golang-fetcher/ 增加 cloud 資料 fetching client（含 GitHub/R2/Vercel/Snyk）

    測試用 curl 或 httpie 指令，模擬整體流程

---

backend-py/
main.py
resume_parser.py
vectorizer.py
ranker.py
letter_generator.py
requirements.txt
docs/
implementation_plan.md
utils/
env_loader.py

檔案 功能說明
main.py 主控流程：載入 .env → 擷取履歷 → 向量化 → 生成 Cover Letter
resume_parser.py 透過 GitHub API 擷取個人公開 repo 描述，作為履歷來源
vectorizer.py 使用 sentence-transformers 模型生成語意向量
ranker.py 將履歷向量與職缺向量做 cosine similarity 排序
letter_generator.py 使用 OpenAI GPT 生成中文 Cover Letter
utils/env_loader.py 載入 .env 環境變數設定
