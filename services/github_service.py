import requests
import logging
from utils.helpers import calculate_account_age
from utils.cache import set_cache, get_cache

BASE_URL = "https://api.github.com"


def get_user_profile(username):
    cache_key = f"user:{username}"

    cached = get_cache(cache_key)
    if cached:
        logging.info(f"Cache hit for {username}")
        return cached
    
    logging.info(f"Fetching user from Github: {username}")

    response = requests.get(f"{BASE_URL}/users/{username}")
    data = handle_github_response(response)

    if not data:
        return None

    result = {
        "username": data["login"],
        "public_repos": data["public_repos"],
        "followers": data["followers"],
        "account_age": calculate_account_age(data["created_at"])
    }

    set_cache(cache_key, result, ttl=120)

    return result


def get_user_top_repos(username, limit=5):
    cache_key = f"repos: {username}:{limit}"

    cached = get_cache(cache_key)

    if cached:
        logging.info(f"Cache hit for repos: {username}")
        return cached
    
    logging.info(f"Fetching repos from Github: {username}")

    response = requests.get(f"{BASE_URL}/users/{username}/repos")
    repos = handle_github_response(response)

    if repos is None:
        return None

    repos_sorted = sorted(
        repos,
        key=lambda x: x["stargazers_count"],
        reverse=True
    )

    top = repos_sorted[:limit]

    result = [
        {
            "name": r["name"],
            "stars": r["stargazers_count"],
            "language": r["language"],
            "repo_url": r["html_url"]
        }
        for r in top
    ]

    set_cache(cache_key, result, ttl=120)

    return result

def handle_github_response(response):
    if response.status_code == 200:
        return response.json()

    if response.status_code == 404:
        return None

    if response.status_code == 403:
        raise Exception("GitHub API rate limit exceeded")

    raise Exception("Unexpected GitHub API error")
