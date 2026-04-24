from utils import fetch_user, fetch_repos, calculate_stats

username = input("Enter GitHub username: ")

user_data = fetch_user(username)

if not user_data:
    print("User not found!")
    exit()

repos_data = fetch_repos(user_data.get("repos_url"))

total_stars, top_language, language_map, top_repos = calculate_stats(repos_data)

print("\n===== GitHub Profile Analysis =====")
print(f"Followers: {user_data.get('followers')}")
print(f"Public Repos: {user_data.get('public_repos')}")
print(f"Total Stars: {total_stars}")
print(f"Top Language: {top_language}")
print(f"Languages Used: {user_data.get(language_map)}")
print(f"Created At: {user_data.get('created_at')}")
print(f"Last Updated: {user_data.get('updated_at')}")

print("\nTop 5 Repositories:")
for i, repo in enumerate(top_repos, start=1):
    print(f"{i}. {repo['name']} ⭐ {repo['stars']}")