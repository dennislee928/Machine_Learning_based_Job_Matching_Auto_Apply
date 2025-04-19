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
