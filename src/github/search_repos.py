# INFRASTRUCTURE
import requests
from typing import Literal
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, RESULTS_PER_PAGE, build_headers


# ORCHESTRATOR
def search_repos_workflow(
    query: str,
    sort_by: Literal["stars", "forks", "updated", "best_match"] = "best_match"
) -> list[TextContent]:
    raw_response = fetch_repositories(query, sort_by)
    formatted_string = format_repo_results(raw_response)
    return [TextContent(type="text", text=formatted_string)]


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

    response = requests.get(url, params=params, headers=build_headers())
    response.raise_for_status()
    return response.json()


# Extract relevant fields from raw API response
def format_repo_results(raw_response: dict) -> str:
    total = raw_response["total_count"]
    items = raw_response.get("items", [])

    lines = []
    lines.append(f"Found {total:,} repositories matching your query.\n")

    if not items:
        lines.append("No results to display.")
        return "\n".join(lines)

    lines.append("Top Results:\n")

    for idx, repo in enumerate(items, 1):
        owner = repo["owner"]["login"]
        name = repo["name"]
        full_name = repo["full_name"]
        desc = repo.get("description", "No description")
        stars = repo["stargazers_count"]
        forks = repo["forks_count"]
        lang = repo.get("language", "Unknown")
        topics = repo.get("topics") or []
        url = repo["html_url"]

        topics_str = ", ".join(topics[:5]) if topics else "None"

        lines.append(f"{idx}. {full_name}")
        lines.append(f"   Description: {desc}")
        lines.append(f"   Language: {lang} | Stars: {stars:,} | Forks: {forks:,}")
        lines.append(f"   Topics: {topics_str}")
        lines.append(f"   URL: {url}")
        lines.append("")

    return "\n".join(lines)
