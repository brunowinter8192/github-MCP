# INFRASTRUCTURE
import requests
import base64
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, build_headers


# ORCHESTRATOR
def get_file_content_workflow(owner: str, repo: str, path: str, metadata_only: bool = False) -> list[TextContent]:
    raw_response = fetch_file_content(owner, repo, path)
    formatter = format_metadata if metadata_only else format_file_response
    formatted_string = formatter(raw_response)
    return [TextContent(type="text", text=formatted_string)]


# FUNCTIONS

# Fetch file content from GitHub Contents API
def fetch_file_content(owner: str, repo: str, path: str) -> dict:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contents/{path}"
    response = requests.get(url, headers=build_headers())
    response.raise_for_status()
    return response.json()


# Format metadata without content decoding
def format_metadata(raw_response: dict) -> str:
    lines = []
    lines.append(f"File: {raw_response['path']}")
    lines.append(f"Name: {raw_response['name']}")
    lines.append(f"Size: {raw_response['size']:,} bytes")
    lines.append(f"Type: {raw_response.get('type', 'unknown')}")
    lines.append(f"SHA: {raw_response.get('sha', 'N/A')}")
    lines.append(f"URL: {raw_response.get('html_url', 'N/A')}")
    return "\n".join(lines)


# Decode base64 content and format response
def format_file_response(raw_response: dict) -> str:
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

    name = raw_response["name"]
    path = raw_response["path"]
    size = raw_response["size"]
    url = raw_response["html_url"]

    lines = []
    lines.append(f"File: {path}")
    lines.append(f"Name: {name}")
    lines.append(f"Size: {size:,} bytes")
    lines.append(f"URL: {url}\n")
    lines.append("Content:")
    lines.append("=" * 60)
    lines.append(decoded_content)
    lines.append("=" * 60)

    return "\n".join(lines)
