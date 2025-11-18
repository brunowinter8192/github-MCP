# INFRASTRUCTURE
import os
import requests
from mcp.types import TextContent

GITHUB_API_BASE = "https://api.github.com"
MAX_TREE_CHARS = 1000
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")


# ORCHESTRATOR
def get_repo_tree_workflow(owner: str, repo: str, path: str = "") -> list[TextContent]:
    default_branch = fetch_default_branch(owner, repo)
    tree_sha = get_tree_sha(owner, repo, default_branch, path)
    raw_tree = fetch_tree(owner, repo, tree_sha)
    formatted_string = format_tree_response(raw_tree, path)
    return [TextContent(type="text", text=formatted_string)]


# FUNCTIONS

# Build headers with optional auth token
def build_headers(accept: str = "application/vnd.github+json") -> dict:
    headers = {
        "Accept": accept,
        "X-GitHub-Api-Version": "2022-11-28"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


# Get default branch name for repository
def fetch_default_branch(owner: str, repo: str) -> str:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    headers = build_headers()

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["default_branch"]


# Get tree SHA for specific path or root
def get_tree_sha(owner: str, repo: str, branch: str, path: str) -> str:
    if not path:
        url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/branches/{branch}"
        headers = build_headers()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()["commit"]["commit"]["tree"]["sha"]

    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contents/{path}"
    params = {"ref": branch}
    headers = build_headers("application/vnd.github.object+json")
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    data = response.json()
    if data.get("type") == "dir":
        return data["sha"]

    raise ValueError(f"Path '{path}' is not a directory")


# Fetch tree structure from GitHub Git Trees API
def fetch_tree(owner: str, repo: str, tree_sha: str) -> dict:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/git/trees/{tree_sha}"
    params = {"recursive": "true"}
    headers = build_headers()

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


# Format tree response with depth limiting if needed
def format_tree_response(raw_tree: dict, base_path: str) -> str:
    tree_items = raw_tree.get("tree", [])

    lines = []
    lines.append(f"Directory: {base_path if base_path else '/'}\n")

    if not tree_items:
        lines.append("Empty directory.")
        return "\n".join(lines)

    dirs = [item for item in tree_items if item["type"] == "tree"]
    files = [item for item in tree_items if item["type"] == "blob"]

    lines.append(f"Directories ({len(dirs)}):")
    for item in dirs[:50]:
        lines.append(f"  {item['path']}/")

    lines.append(f"\nFiles ({len(files)}):")
    for item in files[:50]:
        size = item.get("size", 0)
        lines.append(f"  {item['path']} ({size:,} bytes)")

    current_output = "\n".join(lines)
    if len(current_output) > MAX_TREE_CHARS:
        lines.append(f"\n\nWARNING: Tree truncated (>{MAX_TREE_CHARS} chars).")
        lines.append("Showing top 50 directories and 50 files. Use path parameter to explore subdirectories.")

    return "\n".join(lines)


# Filter tree items to only include depth 0 and 1
def filter_by_depth(items: list, max_depth: int) -> list:
    filtered = []

    for item in items:
        depth = item["path"].count("/")
        if depth <= max_depth:
            filtered.append(item)

    return filtered
