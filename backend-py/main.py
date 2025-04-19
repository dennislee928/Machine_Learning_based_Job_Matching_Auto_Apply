from utils.env_loader import load_env
from resume_parser import fetch_github_profile
from vectorizer import vectorize_text
from ranker import rank_resume
from letter_generator import generate_cover_letter


def main():
    # Load environment variables
    try:
        openai_api_key, github_username = load_env()
    except ValueError as e:
        print(e)
        return

    # Fetch resume from GitHub
    resume_text = fetch_github_profile(github_username)
    if not resume_text:
        print("Failed to fetch resume.")
        return

    # Example job descriptions (replace with actual job descriptions)
    job_descriptions = [
        "Software Engineer with Python experience",
        "AI Researcher with machine learning skills",
        "Data Scientist with data analysis skills",
    ]

    # Vectorize resume and job descriptions
    resume_vector = vectorize_text(resume_text)
    job_vectors = [vectorize_text(job_description) for job_description in job_descriptions]

    # Rank job descriptions
    ranked_jobs, similarity_scores = rank_resume(resume_vector, job_vectors)

    # Generate cover letter for the top job
    top_job_index = ranked_jobs[0]
    top_job_description = job_descriptions[top_job_index]
    cover_letter = generate_cover_letter(resume_text, top_job_description, openai_api_key)

    if cover_letter:
        print("Cover Letter:\n", cover_letter)
    else:
        print("Failed to generate cover letter.")

if __name__ == "__main__":
    main()