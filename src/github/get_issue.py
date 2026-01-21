# INFRASTRUCTURE
import os
import requests
from mcp.types import TextContent

GITHUB_API_BASE = "https://api.github.com"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")


# ORCHESTRATOR
def get_issue_workflow(owner: str, repo: str, issue_number: int) -> list[TextContent]:
    raw_response = fetch_issue(owner, repo, issue_number)
    formatted_string = format_issue(raw_response, owner, repo)
    return [TextContent(type="text", text=formatted_string)]


# FUNCTIONS

# Fetch single issue from GitHub API
def fetch_issue(owner: str, repo: str, issue_number: int) -> dict:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/issues/{issue_number}"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


# Format issue for display
def format_issue(issue: dict, owner: str, repo: str) -> str:
    lines = []

    lines.append(f"# {issue['title']}")
    lines.append(f"State: {issue['state'].upper()} | #{issue['number']}")
    lines.append(f"Author: {issue['user']['login']}")
    lines.append(f"Created: {issue['created_at']} | Updated: {issue['updated_at']}")

    labels = ", ".join(l["name"] for l in issue.get("labels", []))
    if labels:
        lines.append(f"Labels: {labels}")

    lines.append(f"Comments: {issue['comments']}")
    lines.append(f"URL: {issue['html_url']}")

    if issue['comments'] > 0:
        lines.append(f"\n[get_issue_comments: owner=\"{owner}\" repo=\"{repo}\" issue_number={issue['number']}]")

    lines.append("\n---\n")

    body = issue.get("body") or "(No description provided)"
    lines.append(body)

    return "\n".join(lines)
