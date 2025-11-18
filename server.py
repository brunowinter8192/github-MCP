# INFRASTRUCTURE
from typing import Annotated, Literal
from fastmcp import FastMCP
from pydantic import Field
from dotenv import load_dotenv
from mcp.types import TextContent

load_dotenv()

from src.github.search_repos import search_repos_workflow
from src.github.search_code import search_code_workflow
from src.github.get_repo_tree import get_repo_tree_workflow
from src.github.get_file_content import get_file_content_workflow

mcp = FastMCP("GitHub")


# TOOLS

@mcp.tool
def search_repos(
    query: Annotated[str, Field(description="Search query with GitHub qualifiers (e.g., 'machine learning stars:>100 language:python')")],
    sort_by: Annotated[
        Literal["stars", "forks", "updated", "best_match"],
        Field(description="Sort results by: stars (popularity), forks, updated (recent activity), or best_match (relevance)")
    ] = "best_match"
) -> list[TextContent]:
    """Use when user asks to find projects, libraries, frameworks on GitHub. Good for brainstorming, discovering alternatives, finding popular implementations.

IMPORTANT: GitHub search works best with fewer keywords. Start with 1-2 core terms (e.g., 'html parser'), check results, then refine by adding qualifiers (language:python, stars:>100) or narrowing terms. Too many keywords at once yields poor or no results. Iterate: broad query first, then progressively more specific."""
    return search_repos_workflow(query, sort_by)


@mcp.tool
def search_code(
    query: Annotated[str, Field(description="Code search query (e.g., 'def train_model language:python repo:tensorflow/tensorflow')")]
) -> list[TextContent]:
    """Use when user needs specific code examples, implementation patterns, or wants to see how others solved a problem.

IMPORTANT: Start with simple search terms (e.g., 'parse_html language:python'), then narrow down. Overly specific queries with many keywords return few or no results. Iterative refinement: begin broad, add constraints based on initial results."""
    return search_code_workflow(query)


@mcp.tool
def get_repo_tree(
    owner: Annotated[str, Field(description="Repository owner (e.g., 'octocat')")],
    repo: Annotated[str, Field(description="Repository name (e.g., 'Hello-World')")],
    path: Annotated[str, Field(description="Path to explore (empty for root, 'src' for subdirectory)")] = ""
) -> list[TextContent]:
    """Use after search_repos to explore repository structure. Helps understand project layout before diving into specific files."""
    return get_repo_tree_workflow(owner, repo, path)


@mcp.tool
def get_file_content(
    owner: Annotated[str, Field(description="Repository owner (e.g., 'octocat')")],
    repo: Annotated[str, Field(description="Repository name (e.g., 'Hello-World')")],
    path: Annotated[str, Field(description="File path (e.g., 'src/main.py')")]
) -> list[TextContent]:
    """Use to read specific files from repository. Good for analyzing implementations, reading documentation, or extracting code patterns."""
    return get_file_content_workflow(owner, repo, path)


if __name__ == "__main__":
    mcp.run()
