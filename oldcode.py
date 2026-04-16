import requests

username = input("Enter GitHub username: ")
url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code != 200:
    print("User not found!")
    exit()

data = response.json()

repos_url = data.get("repos_url")
repos_response = requests.get(repos_url)
repos_data = repos_response.json()

total_stars = 0
language_count = {}

for repo in repos_data:
    # calculating total stars
    total_stars += repo.get("stargazers_count", 0)
    # finding most used languages
    lang = repo.get("language")
    if lang:
        language_count[lang] = language_count.get(lang, 0) + 1
top_language = max(language_count, key=language_count.get) if language_count else "None"

print("\n===== GitHub Profile Analysis =====")
print(f"Total languages used: {language_count}")
print(f"Top language: {top_language}")
print(f"Total Stars: {total_stars}")
# print(f"{repos_data}")
print(f"Followers: {data.get('followers')}")
print(f"Total no. of repositories: {data.get('public_repos')}")
print(f"Last Update: {data.get('updated_at')}")
print(f"Created At: {data.get('created_at')}")

# Future Implementations:
# Top 5 repos by stars
# Account age (calculate from created_at)
# Sort languages properly
# Pretty CLI formatting
