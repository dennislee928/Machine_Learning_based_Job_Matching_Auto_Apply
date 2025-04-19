import numpy as np
from numpy.linalg import norm

def cosine_similarity(a, b):
    return np.dot(a, b)/(norm(a)*norm(b))


def rank_jobs(resume_vector, job_vectors):
    # Calculate cosine similarity between resume vector and each job vector
    similarity_scores = [cosine_similarity(resume_vector, job_vector) for job_vector in job_vectors]
    # Rank job descriptions based on similarity scores
    ranked_jobs = sorted(range(len(job_vectors)), key=lambda i: similarity_scores[i], reverse=True)
    return ranked_jobs, similarity_scores

if __name__ == '__main__':
    # Example usage
    resume_vector = np.array([0.1, 0.2, 0.3])
    job_vectors = [np.array([0.3, 0.2, 0.1]), np.array([0.1, 0.3, 0.2]), np.array([0.2, 0.1, 0.3])]
    ranked_jobs, similarity_scores = rank_jobs(resume_vector, job_vectors)
    print("Ranked Jobs:\n", ranked_jobs)
    print("Similarity Scores:\n", similarity_scores)
