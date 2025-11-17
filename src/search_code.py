# INFRASTRUCTURE
import os
import requests

GITHUB_API_BASE = "https://api.github.com"
RESULTS_PER_PAGE = 20
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")


# ORCHESTRATOR
def search_code_workflow(query: str) -> dict:
    raw_response = fetch_code_search(query)
    return format_code_results(raw_response)


# FUNCTIONS

# Fetch code search results with text match metadata
def fetch_code_search(query: str) -> dict:
    url = f"{GITHUB_API_BASE}/search/code"
    params = {
        "q": query,
        "per_page": RESULTS_PER_PAGE
    }
    headers = {
        "Accept": "application/vnd.github.text-match+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


# Extract relevant fields from raw API response
def format_code_results(raw_response: dict) -> dict:
    items = []

    for item in raw_response.get("items", []):
        repo = item["repository"]
        text_matches = extract_text_matches(item.get("text_matches", []))

        items.append({
            "owner": repo["owner"]["login"],
            "repo": repo["name"],
            "full_name": repo["full_name"],
            "description": repo.get("description", ""),
            "stars": repo.get("stargazers_count", 0),
            "path": item["path"],
            "file_name": item["name"],
            "html_url": item["html_url"],
            "text_matches": text_matches
        })

    return {
        "total_count": raw_response["total_count"],
        "items": items
    }


# Extract code fragments from text match metadata
def extract_text_matches(matches: list) -> list:
    fragments = []

    for match in matches:
        if match.get("property") in ["content", "path"]:
            fragments.append({
                "fragment": match.get("fragment", ""),
                "property": match.get("property", "")
            })

    return fragments
