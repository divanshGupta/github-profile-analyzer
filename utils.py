import requests


def fetch_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()


def fetch_repos(repos_url):
    response = requests.get(repos_url)

    if response.status_code != 200:
        return []

    return response.json()


def calculate_stats(repos_data):
    total_stars = 0
    language_count = {}

    for repo in repos_data:
        total_stars += repo.get("stargazers_count", 0)

        lang = repo.get("language")
        if lang:
            language_count[lang] = language_count.get(lang, 0) + 1

    top_language = (
        max(language_count, key=language_count.get)
        if language_count
        else "None"
    )

    return total_stars, language_count, top_language