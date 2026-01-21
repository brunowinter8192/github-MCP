---
name: github
description: GitHub API search and exploration tools
---

# GitHub MCP Tools

## Available Tools

| Tool | Purpose |
|------|---------|
| `mcp__github__search_repos` | Find repositories by keywords, stars, language |
| `mcp__github__search_code` | Find code snippets across GitHub |
| `mcp__github__get_repo_tree` | Browse repository file structure |
| `mcp__github__get_file_content` | Read file contents from a repo |
| `mcp__github__search_issues` | Find issues across repositories |
| `mcp__github__get_issue` | Get single issue details |
| `mcp__github__get_issue_comments` | Get comments on an issue |
| `mcp__github__search_prs` | Find pull requests across repositories |
| `mcp__github__list_repo_prs` | List PRs in a specific repo |
| `mcp__github__get_pr` | Get single PR details |
| `mcp__github__get_pr_files` | Get files changed in a PR |

---

## Search Tools

### `mcp__github__search_repos`

Find repositories matching search criteria.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Search query with GitHub qualifiers (e.g., "fastapi stars:>1000 language:python") |
| `sort_by` | string | No | Sort by: stars, forks, updated, best_match (default) |

**Example:**
```
mcp__github__search_repos(query="mcp server language:python", sort_by="stars")
```

---

### `mcp__github__search_code`

Find code snippets across all public repositories.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Code search query (e.g., "FastMCP language:python") |

**Example:**
```
mcp__github__search_code(query="@mcp.tool language:python")
```

---

### `mcp__github__search_issues`

Find issues across repositories.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Issue search query (e.g., "bug is:open repo:owner/repo") |
| `sort_by` | string | No | Sort by: comments, reactions, created, updated, best_match (default) |

**Example:**
```
mcp__github__search_issues(query="memory leak is:open language:python", sort_by="reactions")
```

---

### `mcp__github__search_prs`

Find pull requests across repositories.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | PR search query (e.g., "fix is:merged repo:owner/repo") |
| `sort_by` | string | No | Sort by: comments, reactions, created, updated, best_match (default) |

**Example:**
```
mcp__github__search_prs(query="feature is:open repo:anthropics/claude-code", sort_by="updated")
```

---

## Repository Tools

### `mcp__github__get_repo_tree`

Browse repository file structure.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `owner` | string | Yes | Repository owner (e.g., "anthropics") |
| `repo` | string | Yes | Repository name (e.g., "claude-code") |
| `path` | string | No | Subdirectory path (default: root) |

**Example:**
```
mcp__github__get_repo_tree(owner="fastmcp", repo="fastmcp", path="src")
```

---

### `mcp__github__get_file_content`

Read file contents from a repository.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `owner` | string | Yes | Repository owner |
| `repo` | string | Yes | Repository name |
| `path` | string | Yes | File path (e.g., "src/main.py") |

**Example:**
```
mcp__github__get_file_content(owner="fastmcp", repo="fastmcp", path="README.md")
```

---

## Issue Tools

### `mcp__github__get_issue`

Get details of a single issue.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `owner` | string | Yes | Repository owner |
| `repo` | string | Yes | Repository name |
| `issue_number` | int | Yes | Issue number |

**Example:**
```
mcp__github__get_issue(owner="anthropics", repo="claude-code", issue_number=123)
```

---

### `mcp__github__get_issue_comments`

Get all comments on an issue.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `owner` | string | Yes | Repository owner |
| `repo` | string | Yes | Repository name |
| `issue_number` | int | Yes | Issue number |

**Example:**
```
mcp__github__get_issue_comments(owner="anthropics", repo="claude-code", issue_number=123)
```

---

## Pull Request Tools

### `mcp__github__list_repo_prs`

List pull requests in a specific repository.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `owner` | string | Yes | Repository owner |
| `repo` | string | Yes | Repository name |
| `state` | string | No | Filter by: open, closed, all (default: open) |
| `sort_by` | string | No | Sort by: created, updated, popularity, long-running (default: created) |

**Example:**
```
mcp__github__list_repo_prs(owner="anthropics", repo="claude-code", state="open", sort_by="updated")
```

---

### `mcp__github__get_pr`

Get details of a single pull request.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `owner` | string | Yes | Repository owner |
| `repo` | string | Yes | Repository name |
| `pull_number` | int | Yes | PR number |

**Example:**
```
mcp__github__get_pr(owner="anthropics", repo="claude-code", pull_number=456)
```

---

### `mcp__github__get_pr_files`

Get list of files changed in a pull request.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `owner` | string | Yes | Repository owner |
| `repo` | string | Yes | Repository name |
| `pull_number` | int | Yes | PR number |

**Example:**
```
mcp__github__get_pr_files(owner="anthropics", repo="claude-code", pull_number=456)
```

---

## When to Use

**Use GitHub tools when:**
- User asks to find repositories, libraries, or frameworks
- User needs code examples or implementation patterns
- User wants to explore a repository structure
- User asks about issues or PRs in a project
- Researching how others solved a problem

**Do NOT use when:**
- Information is in local codebase (use Grep/Read)
- User asks about general programming concepts (use training data)
- User wants to create/modify GitHub content (these tools are read-only)

---

## Typical Workflows

### Find and explore a library
1. `search_repos` - Find candidates
2. `get_repo_tree` - Browse structure
3. `get_file_content` - Read specific files

### Research an issue
1. `search_issues` - Find relevant issues
2. `get_issue` - Get details
3. `get_issue_comments` - Read discussion

### Review a PR
1. `get_pr` - Get PR details
2. `get_pr_files` - See changed files
3. `get_file_content` - Read specific changes
