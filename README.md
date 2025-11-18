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

## Configuration

Environment variable: `GITHUB_TOKEN` (optional, for higher rate limits)

### MCP Registration

**.mcp.json.github** - Example configuration for registering GitHub MCP in other projects:
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

**.mcp.json** - Active MCPs used for developing this MCP server (initially empty).

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

See `DOCS.md` for complete module documentation.
