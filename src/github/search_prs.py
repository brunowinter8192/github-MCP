# INFRASTRUCTURE
import os
import requests
from typing import Literal
from mcp.types import TextContent

GITHUB_API_BASE = "https://api.github.com"
RESULTS_PER_PAGE = 20
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")


# ORCHESTRATOR
def search_prs_workflow(
    query: str,
    sort_by: Literal["comments", "reactions", "created", "updated", "best_match"] = "best_match"
) -> list[TextContent]:
    search_query = build_query(query)
    raw_response = fetch_prs(search_query, sort_by)
    formatted_string = format_pr_results(raw_response)
    return [TextContent(type="text", text=formatted_string)]


# FUNCTIONS

# Build search query with is:pr qualifier if not already present
def build_query(query: str) -> str:
    if "is:issue" in query:
        return query.replace("is:issue", "is:pr")
    if "is:pr" not in query and "is:pull-request" not in query:
        return f"{query} is:pr"
    return query


# Fetch PRs from GitHub Search API
def fetch_prs(query: str, sort_by: str) -> dict:
    url = f"{GITHUB_API_BASE}/search/issues"
    params = {"q": query, "per_page": RESULTS_PER_PAGE, "order": "desc"}
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


# Format search results for display
def format_pr_results(raw_response: dict) -> str:
    total = raw_response["total_count"]
    items = raw_response.get("items", [])

    lines = []
    lines.append(f"Found {total:,} pull requests matching your query.\n")

    if not items:
        lines.append("No results to display.")
        return "\n".join(lines)

    lines.append("Top Results:\n")

    for idx, pr in enumerate(items, 1):
        repo_url = pr["repository_url"]
        repo_name = repo_url.split("/repos/")[1]
        owner, repo = repo_name.split("/")

        state = pr["state"].upper()
        if pr.get("pull_request", {}).get("merged_at"):
            state = "MERGED"

        lines.append(f"{idx}. [{state}] {pr['title']}")
        lines.append(f"   Repo: {repo_name} | #{pr['number']}")
        lines.append(f"   Author: {pr['user']['login']} | Comments: {pr['comments']}")

        labels = ", ".join(l["name"] for l in pr.get("labels", []))
        if labels:
            lines.append(f"   Labels: {labels}")

        lines.append(f"   URL: {pr['html_url']}")
        lines.append(f"   [get_pr: owner=\"{owner}\" repo=\"{repo}\" pull_number={pr['number']}]")
        lines.append("")

    return "\n".join(lines)
