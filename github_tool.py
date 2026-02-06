import requests


def github_search(query: str, limit: int = 3):
    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc"
    }

    response = requests.get(url, params=params)
    data = response.json()

    repos = []
    for item in data.get("items", [])[:limit]:
        repos.append({
            "name": item["name"],
            "url": item["html_url"],
            "stars": item["stargazers_count"]
        })

    return repos
