from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
import json
import os

from utils.env_loader import load_env
from resume_parser import fetch_github_profile
from vectorizer import generate_vector
from ranker import rank_jobs
from letter_generator import generate_cover_letter

app = FastAPI(
    title="Job Matcher API",
    description="API for matching resumes with job descriptions and generating cover letters",
    version="0.1.0"
)

class JobDescription(BaseModel):
    id: int
    title: str
    company: str
    description: str

class JobRankingResult(BaseModel):
    job_id: int
    job_title: str
    company: str
    similarity_score: float

class CoverLetterRequest(BaseModel):
    resume_text: str
    job_description: str

class CoverLetterResponse(BaseModel):
    cover_letter: str

def get_credentials():
    try:
        openai_api_key, github_username = load_env()
        return openai_api_key, github_username
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "歡迎使用職缺匹配 API"}

@app.get("/jobs", response_model=List[JobDescription])
async def get_jobs():
    try:
        with open("docs/jobs.json", "r", encoding="utf-8") as f:
            jobs = json.load(f)
        return jobs
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"載入職缺資料失敗: {str(e)}")

@app.get("/match", response_model=List[JobRankingResult])
async def match_jobs(github_username: Optional[str] = None):
    try:
        openai_api_key, default_github_username = get_credentials()
        
        # 使用提供的 GitHub 用戶名或預設值
        username = github_username or default_github_username
        
        # 獲取履歷
        resume_text = fetch_github_profile(username)
        if not resume_text:
            raise HTTPException(status_code=404, detail=f"無法獲取 GitHub 用戶 {username} 的資料")
        
        # 載入職缺
        with open("docs/jobs.json", "r", encoding="utf-8") as f:
            jobs = json.load(f)
        
        job_descriptions = [job["description"] for job in jobs]
        
        # 向量化
        resume_vector = generate_vector(resume_text)
        job_vectors = [generate_vector(description) for description in job_descriptions]
        
        # 排名
        ranked_indices, similarity_scores = rank_jobs(resume_vector, job_vectors)
        
        # 構建結果
        results = []
        for i, idx in enumerate(ranked_indices):
            job = jobs[idx]
            results.append(JobRankingResult(
                job_id=job["id"],
                job_title=job["title"],
                company=job["company"],
                similarity_score=float(similarity_scores[idx])
            ))
        
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"職缺匹配失敗: {str(e)}")

@app.post("/generate-cover-letter", response_model=CoverLetterResponse)
async def create_cover_letter(request: CoverLetterRequest):
    try:
        openai_api_key, _ = get_credentials()
        
        cover_letter = generate_cover_letter(
            resume_text=request.resume_text,
            job_description=request.job_description,
            openai_api_key=openai_api_key
        )
        
        if not cover_letter:
            raise HTTPException(status_code=500, detail="生成求職信失敗")
        
        return CoverLetterResponse(cover_letter=cover_letter)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"生成求職信時發生錯誤: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 