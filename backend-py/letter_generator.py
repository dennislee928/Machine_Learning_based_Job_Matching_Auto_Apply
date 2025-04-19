import openai

def generate_cover_letter(resume_text, job_description, openai_api_key):
    openai.api_key = openai_api_key

    prompt = f"""Write a cover letter for a job application.
    Resume Text: {resume_text}
    Job Description: {job_description}
    """

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or another suitable engine
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        cover_letter = response.choices[0].text.strip()
        return cover_letter
    except Exception as e:
        print(f"Error generating cover letter: {e}")
        return None

if __name__ == '__main__':
    # Example usage
    resume_text = "Experienced software engineer with a passion for AI."
    job_description = "Looking for a software engineer with AI experience."
    openai_api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual API key
    cover_letter = generate_cover_letter(resume_text, job_description, openai_api_key)
    if cover_letter:
        print("Cover Letter:\n", cover_letter)
    else:
        print("Failed to generate cover letter.")
