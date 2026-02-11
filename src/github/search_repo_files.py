# INFRASTRUCTURE
from fnmatch import fnmatch
from os.path import basename
from mcp.types import TextContent
from src.github.get_repo_tree import fetch_default_branch, get_tree_sha, fetch_tree

RESULTS_LIMIT = 50


# ORCHESTRATOR
def search_repo_files_workflow(owner: str, repo: str, pattern: str, path: str = "") -> list[TextContent]:
    default_branch = fetch_default_branch(owner, repo)
    tree_sha = get_tree_sha(owner, repo, default_branch, path)
    raw_tree = fetch_tree(owner, repo, tree_sha, recursive=True)
    matches = filter_by_pattern(raw_tree, pattern)
    return [TextContent(type="text", text=format_matches(matches, pattern, path))]


# FUNCTIONS

# Filter tree items by glob pattern against filename or full path
def filter_by_pattern(raw_tree: dict, pattern: str) -> list[dict]:
    items = [item for item in raw_tree.get("tree", []) if item["type"] == "blob"]
    has_slash = "/" in pattern
    return [
        item for item in items
        if fnmatch(item["path"] if has_slash else basename(item["path"]), pattern)
    ][:RESULTS_LIMIT]


# Format matching files as text output
def format_matches(matches: list[dict], pattern: str, base_path: str) -> str:
    lines = []
    scope = base_path if base_path else "/"
    lines.append(f"Search: \"{pattern}\" in {scope}\n")

    if not matches:
        lines.append("No files found.")
        return "\n".join(lines)

    lines.append(f"Matches ({len(matches)}):")
    for item in matches:
        size = item.get("size", 0)
        lines.append(f"  {item['path']} ({size:,} bytes)")

    return "\n".join(lines)
