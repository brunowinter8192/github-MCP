# INFRASTRUCTURE
import os
import requests
from mcp.types import TextContent

GITHUB_API_BASE = "https://api.github.com"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
COMMENTS_PER_PAGE = 30


# ORCHESTRATOR
def get_issue_comments_workflow(owner: str, repo: str, issue_number: int) -> list[TextContent]:
    raw_response = fetch_comments(owner, repo, issue_number)
    formatted_string = format_comments(raw_response, owner, repo, issue_number)
    return [TextContent(type="text", text=formatted_string)]


# FUNCTIONS

# Fetch comments from GitHub API
def fetch_comments(owner: str, repo: str, issue_number: int) -> list:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/issues/{issue_number}/comments"
    params = {"per_page": COMMENTS_PER_PAGE}
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


# Format comments for display
def format_comments(comments: list, owner: str, repo: str, issue_number: int) -> str:
    lines = []

    lines.append(f"# Comments on {owner}/{repo}#{issue_number}")
    lines.append(f"Total: {len(comments)} comments\n")

    if not comments:
        lines.append("No comments on this issue.")
        return "\n".join(lines)

    for idx, comment in enumerate(comments, 1):
        lines.append(f"--- Comment {idx} ---")
        lines.append(f"Author: {comment['user']['login']}")
        lines.append(f"Date: {comment['created_at']}")
        lines.append("")
        lines.append(comment.get("body") or "(Empty comment)")
        lines.append("")

    return "\n".join(lines)
