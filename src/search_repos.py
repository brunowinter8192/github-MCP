# INFRASTRUCTURE
import os
import requests
from typing import Literal

GITHUB_API_BASE = "https://api.github.com"
RESULTS_PER_PAGE = 20
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")


# ORCHESTRATOR
def search_repos_workflow(
    query: str,
    sort_by: Literal["stars", "forks", "updated", "best_match"] = "best_match"
) -> dict:
    raw_response = fetch_repositories(query, sort_by)
    return format_repo_results(raw_response)


# FUNCTIONS

# Fetch repositories from GitHub Search API
def fetch_repositories(query: str, sort_by: str) -> dict:
    url = f"{GITHUB_API_BASE}/search/repositories"

    params = {
        "q": query,
        "per_page": RESULTS_PER_PAGE,
        "order": "desc"
    }

    if sort_by != "best_match":
        params["sort"] = sort_by

    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


# Extract relevant fields from raw API response
def format_repo_results(raw_response: dict) -> dict:
    items = []

    for repo in raw_response.get("items", []):
        items.append({
            "owner": repo["owner"]["login"],
            "repo": repo["name"],
            "full_name": repo["full_name"],
            "description": repo.get("description", ""),
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "language": repo.get("language", ""),
            "updated_at": repo["updated_at"],
            "html_url": repo["html_url"]
        })

    return {
        "total_count": raw_response["total_count"],
        "items": items
    }
