import requests
from datetime import datetime

def fetch_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()

import requests

def fetch_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    repos = response.json()

    # sort by stars (descending)
    repos_sorted = sorted(repos, key=lambda x: x["stargazers_count"], reverse=True)

    # take top 5
    top_repos = repos_sorted[:5]

    # clean response
    formatted = []
    for repo in top_repos:
        formatted.append({
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "language": repo["language"],
            "repo_url": repo["html_url"],
            "created_at": repo["created_at"]
        })

    return formatted

# def calculate_stats(repos_data):
#     total_stars = 0
#     language_count = {}

#     for repo in repos_data:
#         total_stars += repo.get("stargazers_count", 0)

#         lang = repo.get("language")
#         if lang:
#             language_count[lang] = language_count.get(lang, 0) + 1

#     top_language = (
#         max(language_count, key=language_count.get)
#         if language_count
#         else "None"
#     )

#     return total_stars, language_count, top_language

def calculate_stats(repos_data):
    total_stars = 0
    
    language_map = {}

    repo_list = []

    for repo in repos_data:
        stars = repo.get("stargazers_count", 0)
        total_stars += stars

        # collect repo info
        repo_list.append({
            "name": repo.get("name"),
            "stars": stars
        })

        # language counting
        lang = repo.get("language")
        if lang:
            language_map[lang] = language_map.get(lang, 0) + 1

    # top language
    top_language = (
        max(language_map, key=language_map.get)
        if language_map
        else "None"
    )

    # sort repos by stars (descending)
    top_repos = sorted(repo_list, key=lambda x: x["stars"], reverse=True)[:5]

    return total_stars, language_map, top_language, top_repos

def calculate_account_age(created_at):
    created_date = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
    today = datetime.utcnow()

    age_years = today.year - created_date.year

    # adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (created_date.month, created_date.day):
        age_years -= 1

    return age_years