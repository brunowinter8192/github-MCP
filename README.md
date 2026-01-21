# GitHub MCP Server

GitHub API tools for code discovery and repository exploration.

**Remote:** https://github.com/brunowinter8192/github-MCP

After major changes, push to remote:
```bash
git add -A && git commit -m "Your message" && git push
```

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

Returns repositories with owner, repo name, description, stars, URL as formatted JSON string.

**Search Strategy:** Start with 1-2 core keywords (e.g., 'html parser'), check results, then refine by adding qualifiers (language:python, stars:>100). Too many keywords at once yields poor results. Iterate: broad query first, then progressively more specific.

### search_code
Search code across GitHub repositories.

Parameters:
- `query`: Code search query (e.g., 'def train_model language:python repo:tensorflow/tensorflow')

Returns code matches with repository info, file path, and text matches as formatted JSON string.

**Search Strategy:** Start with simple search terms (e.g., 'parse_html language:python'), then narrow down. Overly specific queries return few results. Iterative refinement yields better matches.

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

### search_issues
Search GitHub issues and discussions.

Parameters:
- `query`: Search string with qualifiers (e.g., 'authentication bug repo:owner/repo state:open')
- `sort_by`: comments | reactions | created | updated | best_match (default: best_match)

Returns issues with repository, number, title, state, author, comments count, labels, and URL.

**Note:** By default only searches issues (not PRs). Add 'is:pr' to include pull requests. Use repo:owner/repo to search specific repository.

### get_issue
Read a specific issue with full body content.

Parameters:
- `owner`: Repository owner (e.g., 'anthropics')
- `repo`: Repository name (e.g., 'claude-code')
- `issue_number`: Issue number (e.g., 11712)

Returns issue title, state, author, dates, labels, comments count, URL, and full body content.

### get_issue_comments
Read all comments on an issue.

Parameters:
- `owner`: Repository owner
- `repo`: Repository name
- `issue_number`: Issue number

Returns list of comments with author, date, and full body content.

### search_prs
Search pull requests across GitHub.

Parameters:
- `query`: Search string with qualifiers (e.g., 'fix authentication repo:owner/repo is:merged')
- `sort_by`: comments | reactions | created | updated | best_match (default: best_match)

Returns PRs with repository, number, title, state, author, comments count, labels, and URL.

**Note:** Searches PRs globally. Use repo:owner/repo to search specific repository. Use is:merged to find completed PRs.

### list_repo_prs
List pull requests in a specific repository.

Parameters:
- `owner`: Repository owner (e.g., 'facebook')
- `repo`: Repository name (e.g., 'react')
- `state`: open | closed | all (default: open)
- `sort_by`: created | updated | popularity | long-running (default: created)

Returns PRs with number, title, state, author, branches, creation date, labels, and URL.

### get_pr
Read a specific pull request with full body content.

Parameters:
- `owner`: Repository owner
- `repo`: Repository name
- `pull_number`: Pull request number

Returns PR title, state, author, branches, dates, merge info, commits, additions, deletions, changed files, and full body content.

### get_pr_files
List files changed in a pull request.

Parameters:
- `owner`: Repository owner
- `repo`: Repository name
- `pull_number`: Pull request number

Returns list of changed files with filename, status (added/modified/removed), additions, deletions, and patch preview.

## Configuration

Environment variable: `GITHUB_TOKEN` (optional, for higher rate limits)

### MCP Registration

Add to your project's `.mcp.json`:
```json
{
  "mcpServers": {
    "github": {
      "command": "/path/to/venv/bin/fastmcp",
      "args": ["run", "/path/to/github/server.py"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

## Bug Fixes

Bug fix documentation is stored in `bug_fixes/` directory. Each fix is documented with:
- Problem description
- Root cause analysis
- Fix implementation with file:line references

## Debug Scripts

Debug and test scripts are stored in `debug/` directories (gitignored):
- **Simple MCP:** Root-level `debug/` folder
- **Complex MCP:** Per-module `src/[module]/debug/` folders for multi-API-domain servers

## Documentation

Module documentation is located in `src/github/DOCS.md`.
