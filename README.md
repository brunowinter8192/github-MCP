# GitHub Research Plugin

GitHub API tools for Claude Code - search repos, code, issues, PRs.

**Status:** In active development

## Installation

### Option A: Global (all projects)

```bash
/plugin install github-research@brunowinter-plugins
```

### Option B: Project-scoped (only this project)

```bash
/plugin install github-research@brunowinter-plugins --scope project
```

### Scope Overview

| Scope | Location | Visibility |
|-------|----------|------------|
| user | ~/.claude/settings.json | Only you, all projects |
| project | .claude/settings.json | All collaborators |
| local | .claude/settings.local.json | Only you, only this project |

## Quick Start

1. Install plugin (see above)
2. Activate: Type `ghs` in prompt or `/github-research:gh-search`

## Plugin Components

| Component | Description |
|-----------|-------------|
| **Skill** | `/github-research:gh-search` - Tool usage context and workflows |
| **MCP Server** | 11 GitHub API tools |
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

- **Trigger:** `ghs` in prompt
- **Manual:** `/github-research:gh-search`
- **Content:** Tool context, workflows, when-to-use guidance

### MCP Server

- 11 read-only GitHub API tools
- **Optional:** `GITHUB_TOKEN` env var for higher rate limits

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
│   └── agents/github-search.md
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

## Development

Local testing without installation:

```bash
claude --plugin-dir ./github
```
