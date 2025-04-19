import requests

def fetch_github_profile(username):
    try:
        response = requests.get(f'https://api.github.com/users/{username}')
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        # Extract relevant information from the GitHub profile
        bio = data.get('bio', '')
        name = data.get('name', '')
        location = data.get('location', '')
        # You can add more fields as needed
        resume_text = f"{name}\n{location}\n{bio}"
        return resume_text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching GitHub profile: {e}")
        return None

if __name__ == '__main__':
    # Example usage
    username = 'your_github_username'  # Replace with a valid GitHub username
    resume = fetch_github_profile(username)
    if resume:
        print("Resume:\n", resume)
    else:
        print("Failed to fetch resume.")
