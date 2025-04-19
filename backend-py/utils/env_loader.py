import os
from dotenv import load_dotenv

def load_env():
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    github_username = os.getenv("GITHUB_USERNAME")
    if not openai_api_key or not github_username:
        raise ValueError("Missing environment variables. Please set OPENAI_API_KEY and GITHUB_USERNAME in .env file.")
    return openai_api_key, github_username

if __name__ == '__main__':
    openai_api_key, github_username = load_env()
    print(f"OpenAI API Key: {openai_api_key[:5]}...{openai_api_key[-5:]}")
    print(f"GitHub Username: {github_username}")
