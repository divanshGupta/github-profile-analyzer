from utils import fetch_user, fetch_repos, calculate_stats

username = input("Enter GitHub username: ")

user_data = fetch_user(username)

if not user_data:
    print("User not found!")
    exit()

repos_data = fetch_repos(user_data.get("repos_url"))

total_stars, language_count, top_language = calculate_stats(repos_data)

print("\n===== GitHub Profile Analysis =====")
print(f"Followers: {user_data.get('followers')}")
print(f"Public Repos: {user_data.get('public_repos')}")
print(f"Total Stars: {total_stars}")
print(f"Top Language: {top_language}")
print(f"Languages Used: {language_count}")
print(f"Created At: {user_data.get('created_at')}")
print(f"Last Updated: {user_data.get('updated_at')}")