import json
from vectorizer import generate_vector
from ranker import rank_jobs

# 模擬履歷內容（可改為你 GitHub 抓下來的結果）
resume_text = """
熟悉使用 Golang 開發 RESTful API，部署於 Render 與 Fly.io。
具備 DevOps 實務經驗：Cloudflare Pages, Supabase, Terraform, GitHub Actions。
有資安實務背景，整合 Snyk、WAF、DNSlog 做自動化掃描。
"""

# 讀取模擬職缺描述
with open("docs/jobs.json", "r") as f:
    jobs = json.load(f)

job_texts = [job["description"] for job in jobs]
job_vectors = [generate_vector(text) for text in job_texts]
resume_vector = generate_vector(resume_text)

# 做推薦排序
ranked_indices, scores = rank_jobs(resume_vector, job_vectors)

print("\n📊 排名結果：")
for i, idx in enumerate(ranked_indices):
    job = jobs[idx]
    print(f"{i+1}. [{job['title']}] @ {job['company']}｜相似度: {scores[idx]:.4f}")
