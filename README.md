# GitHub MCP Server

GitHub API tools for code discovery and repository exploration.

## Prerequisites

- Python 3.10+
- GitHub Personal Access Token (optional, increases rate limits)

## Quick Start

1. Install dependencies:
```bash
pip install fastmcp requests pydantic python-dotenv
```

2. Set environment variable (optional):
```bash
export GITHUB_TOKEN=your_token_here
```

3. Run MCP server:
```bash
fastmcp run server.py
```

## Tools

### search_repos
Find repositories by query with GitHub qualifiers.

Parameters:
- `query`: Search string with qualifiers (e.g., 'machine learning stars:>100 language:python')
- `sort_by`: stars | forks | updated | best_match (default: best_match)

Returns repositories with owner, repo name, description, stars, URL.

### search_code
Search code across GitHub repositories.

Parameters:
- `query`: Code search query (e.g., 'def train_model language:python repo:tensorflow/tensorflow')

Returns code matches with repository info, file path, and text matches.

### get_repo_tree
Explore repository file structure.

Parameters:
- `owner`: Repository owner (e.g., 'octocat')
- `repo`: Repository name (e.g., 'Hello-World')
- `path`: Path to explore (default: root)

Returns tree structure with files and directories.

### get_file_content
Read specific file content from repository.

Parameters:
- `owner`: Repository owner
- `repo`: Repository name
- `path`: File path (e.g., 'src/main.py')

Returns file content with metadata.

## Configuration

Environment variable: `GITHUB_TOKEN` (optional, for higher rate limits)

## Documentation

See `DOCS.md` for complete module documentation.
