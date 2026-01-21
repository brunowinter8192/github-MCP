# INFRASTRUCTURE
import os
import requests
from typing import Literal
from mcp.types import TextContent

GITHUB_API_BASE = "https://api.github.com"
RESULTS_PER_PAGE = 20
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")


# ORCHESTRATOR
def search_issues_workflow(
    query: str,
    sort_by: Literal["comments", "reactions", "created", "updated", "best_match"] = "best_match"
) -> list[TextContent]:
    search_query = build_query(query)
    raw_response = fetch_issues(search_query, sort_by)
    formatted_string = format_issue_results(raw_response)
    return [TextContent(type="text", text=formatted_string)]


# FUNCTIONS

# Build search query with is:issue qualifier if not already present
def build_query(query: str) -> str:
    if "is:pr" in query or "is:pull-request" in query:
        return query
    if "is:issue" not in query:
        return f"{query} is:issue"
    return query


# Fetch issues from GitHub Search API
def fetch_issues(query: str, sort_by: str) -> dict:
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
def format_issue_results(raw_response: dict) -> str:
    total = raw_response["total_count"]
    items = raw_response.get("items", [])

    lines = []
    lines.append(f"Found {total:,} issues matching your query.\n")

    if not items:
        lines.append("No results to display.")
        return "\n".join(lines)

    lines.append("Top Results:\n")

    for idx, issue in enumerate(items, 1):
        repo_url = issue["repository_url"]
        repo_name = repo_url.split("/repos/")[1]
        owner, repo = repo_name.split("/")

        lines.append(f"{idx}. [{issue['state'].upper()}] {issue['title']}")
        lines.append(f"   Repo: {repo_name} | #{issue['number']}")
        lines.append(f"   Author: {issue['user']['login']} | Comments: {issue['comments']}")

        labels = ", ".join(l["name"] for l in issue.get("labels", []))
        if labels:
            lines.append(f"   Labels: {labels}")

        lines.append(f"   URL: {issue['html_url']}")
        lines.append(f"   [get_issue: owner=\"{owner}\" repo=\"{repo}\" issue_number={issue['number']}]")
        lines.append("")

    return "\n".join(lines)
