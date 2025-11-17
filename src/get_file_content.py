# INFRASTRUCTURE
import os
import requests
import base64

GITHUB_API_BASE = "https://api.github.com"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")


# ORCHESTRATOR
def get_file_content_workflow(owner: str, repo: str, path: str) -> dict:
    raw_response = fetch_file_content(owner, repo, path)
    return format_file_response(raw_response)


# FUNCTIONS

# Fetch file content from GitHub Contents API
def fetch_file_content(owner: str, repo: str, path: str) -> dict:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contents/{path}"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


# Decode base64 content and format response
def format_file_response(raw_response: dict) -> dict:
    if raw_response.get("type") != "file":
        raise ValueError(f"Path is not a file, got type: {raw_response.get('type')}")

    content = raw_response.get("content", "")
    encoding = raw_response.get("encoding", "")

    decoded_content = ""
    if encoding == "base64" and content:
        content_clean = content.replace("\n", "")
        decoded_content = base64.b64decode(content_clean).decode("utf-8")
    else:
        decoded_content = content

    return {
        "name": raw_response["name"],
        "path": raw_response["path"],
        "size": raw_response["size"],
        "content": decoded_content,
        "sha": raw_response["sha"],
        "html_url": raw_response["html_url"]
    }
