# INFRASTRUCTURE
from typing import Literal
from fastmcp import FastMCP
from dotenv import load_dotenv
from mcp.types import TextContent

load_dotenv()

from src.github.search_repos import search_repos_workflow
from src.github.search_code import search_code_workflow
from src.github.get_repo_tree import get_repo_tree_workflow
from src.github.get_file_content import get_file_content_workflow
from src.github.search_issues import search_issues_workflow
from src.github.get_issue import get_issue_workflow
from src.github.get_issue_comments import get_issue_comments_workflow
from src.github.search_prs import search_prs_workflow
from src.github.list_repo_prs import list_repo_prs_workflow
from src.github.get_pr import get_pr_workflow
from src.github.get_pr_files import get_pr_files_workflow

mcp = FastMCP("GitHub")


# TOOLS

@mcp.tool
def search_repos(
    query: str,
    sort_by: Literal["stars", "forks", "updated", "best_match"] = "best_match"
) -> list[TextContent]:
    """Search repos."""
    return search_repos_workflow(query, sort_by)


@mcp.tool
def search_code(query: str) -> list[TextContent]:
    """Search code."""
    return search_code_workflow(query)


@mcp.tool
def get_repo_tree(owner: str, repo: str, path: str = "") -> list[TextContent]:
    """Get repo tree."""
    return get_repo_tree_workflow(owner, repo, path)


@mcp.tool
def get_file_content(owner: str, repo: str, path: str) -> list[TextContent]:
    """Get file content."""
    return get_file_content_workflow(owner, repo, path)


@mcp.tool
def search_issues(
    query: str,
    sort_by: Literal["comments", "reactions", "created", "updated", "best_match"] = "best_match"
) -> list[TextContent]:
    """Search issues."""
    return search_issues_workflow(query, sort_by)


@mcp.tool
def get_issue(owner: str, repo: str, issue_number: int) -> list[TextContent]:
    """Get issue."""
    return get_issue_workflow(owner, repo, issue_number)


@mcp.tool
def get_issue_comments(owner: str, repo: str, issue_number: int) -> list[TextContent]:
    """Get issue comments."""
    return get_issue_comments_workflow(owner, repo, issue_number)


@mcp.tool
def search_prs(
    query: str,
    sort_by: Literal["comments", "reactions", "created", "updated", "best_match"] = "best_match"
) -> list[TextContent]:
    """Search PRs."""
    return search_prs_workflow(query, sort_by)


@mcp.tool
def list_repo_prs(
    owner: str,
    repo: str,
    state: Literal["open", "closed", "all"] = "open",
    sort_by: Literal["created", "updated", "popularity", "long-running"] = "created"
) -> list[TextContent]:
    """List repo PRs."""
    return list_repo_prs_workflow(owner, repo, state, sort_by)


@mcp.tool
def get_pr(owner: str, repo: str, pull_number: int) -> list[TextContent]:
    """Get PR."""
    return get_pr_workflow(owner, repo, pull_number)


@mcp.tool
def get_pr_files(owner: str, repo: str, pull_number: int) -> list[TextContent]:
    """Get PR files."""
    return get_pr_files_workflow(owner, repo, pull_number)


if __name__ == "__main__":
    mcp.run()
