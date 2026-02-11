# INFRASTRUCTURE
import requests
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, build_headers

MAX_TREE_CHARS = 1000


# ORCHESTRATOR
def get_repo_tree_workflow(owner: str, repo: str, path: str = "", depth: int = -1) -> list[TextContent]:
    default_branch = fetch_default_branch(owner, repo)
    tree_sha = get_tree_sha(owner, repo, default_branch, path)
    recursive = depth != 1
    raw_tree = fetch_tree(owner, repo, tree_sha, recursive)
    formatted_string = format_tree_response(raw_tree, path, depth)
    return [TextContent(type="text", text=formatted_string)]


# FUNCTIONS

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
def fetch_tree(owner: str, repo: str, tree_sha: str, recursive: bool = True) -> dict:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/git/trees/{tree_sha}"
    params = {"recursive": "true"} if recursive else {}
    headers = build_headers()

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


# Format tree response with depth filtering and root-level prioritization
def format_tree_response(raw_tree: dict, base_path: str, depth: int = -1) -> str:
    tree_items = raw_tree.get("tree", [])

    lines = []
    lines.append(f"Directory: {base_path if base_path else '/'}\n")

    if not tree_items:
        lines.append("Empty directory.")
        return "\n".join(lines)

    if depth > 0:
        tree_items = [item for item in tree_items if item["path"].count("/") < depth]

    dirs = sorted(
        [item for item in tree_items if item["type"] == "tree"],
        key=lambda item: item["path"].count("/")
    )
    files = sorted(
        [item for item in tree_items if item["type"] == "blob"],
        key=lambda item: item["path"].count("/")
    )

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
        lines.append("Showing top 50 directories and 50 files. Use path parameter or depth=1 to narrow results.")

    return "\n".join(lines)
