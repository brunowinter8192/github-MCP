# GitHub Research Plugin

GitHub API tools for Claude Code - search repos, code, issues, PRs.

## Quick Start

1. Add marketplace:
```bash
/plugin marketplace add brunowinter8192/github-MCP
```

2. Install plugin:
```bash
/plugin install github-research@brunowinter-plugins
```

3. Done. Plugin activates automatically on GitHub-related queries.

## Plugin Components

| Component | Description |
|-----------|-------------|
| **Skill** | `/github-research:github` - Tool usage context and workflows |
| **MCP Server** | 11 GitHub API tools |
| **Hook** | Auto-activates skill on keywords (github, repo, PR, issue) |
| **Subagent** | `github-search` - Deep research specialist |

## Tools

| Tool | Purpose |
|------|---------|
| `search_repos` | Find repositories |
| `search_code` | Find code snippets |
| `get_repo_tree` | Browse repo structure |
| `get_file_content` | Read file content |
| `search_issues` | Find issues |
| `get_issue` | Get issue details |
| `get_issue_comments` | Get issue comments |
| `search_prs` | Find pull requests |
| `list_repo_prs` | List repo PRs |
| `get_pr` | Get PR details |
| `get_pr_files` | Get PR changed files |

## Component Details

### Skill

- **Manual:** `/github-research:github`
- **Auto:** Hook triggers on GitHub keywords
- **Content:** Tool context, workflows, when-to-use guidance

### MCP Server

- 11 read-only GitHub API tools
- **Optional:** `GITHUB_TOKEN` env var for higher rate limits

### Hook

- **Keywords:** github, GitHub, repo, repository, PR, pull request, issue
- **Action:** Activates skill automatically

### Subagent

- **Type:** `github-search`
- **Use for:** Complex multi-tool research, comparing repos
- **Skip for:** Single tool calls, known owner/repo

## MCP Registration (Alternative)

Manual registration without plugin in `.mcp.json`:

```json
{
  "mcpServers": {
    "github": {
      "command": "uvx",
      "args": ["--with", "requests", "--with", "python-dotenv", "fastmcp", "run", "/absolute/path/to/server.py"],
      "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN}" }
    }
  }
}
```

## Directory Structure

```
github/
├── .claude-plugin/           # Plugin distribution
│   ├── plugin.json           # Plugin metadata
│   ├── marketplace.json      # Marketplace entry
│   ├── skills/github/SKILL.md
│   ├── agents/github-search.md
│   └── hooks/hooks.json
├── server.py                 # MCP entry point
└── src/github/               # Tool implementations
    └── DOCS.md
```

## Documentation

| Doc | Content |
|-----|---------|
| `src/github/DOCS.md` | Tool implementation details |
| `.claude-plugin/skills/github/SKILL.md` | Tool usage guide |
| `.claude-plugin/agents/github-search.md` | Subagent instructions |
