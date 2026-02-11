---
name: gh-search
description: GitHub API search and exploration tools
---

# GitHub MCP Tools

## Available Tools

| Tool | Purpose |
|------|---------|
| `mcp__github__search_repos` | Find repositories by keywords, stars, language |
| `mcp__github__search_code` | Find code snippets across GitHub |
| `mcp__github__get_repo` | Get repository metadata (topics, license, etc.) |
| `mcp__github__get_repo_tree` | Browse repository file structure |
| `mcp__github__get_file_content` | Read file contents from a repo |
| `mcp__github__search_issues` | Find issues across repositories |
| `mcp__github__get_issue` | Get single issue details |
| `mcp__github__get_issue_comments` | Get comments on an issue |
| `mcp__github__search_prs` | Find pull requests across repositories |
| `mcp__github__list_repo_prs` | List PRs in a specific repo |
| `mcp__github__get_pr` | Get single PR details |
| `mcp__github__get_pr_files` | Get files changed in a PR |
| `mcp__github__search_discussions` | Find discussions across GitHub |
| `mcp__github__list_discussions` | List discussions in a specific repo |
| `mcp__github__get_discussion` | Get discussion with comments |

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

**Output Parsing:**

Code search returns file paths - extract them for your output:
```
search_code("@mcp.tool language:python")
→ Returns: st3v3nmw/sourcerer-mcp - internal/mcp/server.go
→ Note path: internal/mcp/server.go
→ Include in output: "MCP tools in `internal/mcp/server.go`"
```

Always note the file path, not just the repo name.

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
| `depth` | int | No | Tree depth: -1 = full recursive (default), 1 = direct children only, N = limit to N levels |

**Notes:**
- Results are sorted by depth: root-level files/dirs appear first, deeper items after
- Use `depth=1` to see only immediate contents of a directory (avoids flooding from deep subdirectories)

**Example:**
```
mcp__github__get_repo_tree(owner="fastmcp", repo="fastmcp", path="src")
mcp__github__get_repo_tree(owner="user", repo="big-repo", path="data", depth=1)
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

## Repository Tools

### `mcp__github__get_repo`

Get repository metadata including topics and license.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `owner` | string | Yes | Repository owner |
| `repo` | string | Yes | Repository name |

**Example:**
```
mcp__github__get_repo(owner="anthropics", repo="claude-code")
```

---

## Discussion Tools

### `mcp__github__search_discussions`

Find discussions across all public repositories (Q&A, ideas, announcements).

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Search query with GitHub qualifiers |
| `first` | int | No | Number of results (default: 10, max: 100) |

**Example:**
```
mcp__github__search_discussions(query="MCP server setup", first=5)
```

---

### `mcp__github__list_discussions`

List discussions in a specific repository.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `owner` | string | Yes | Repository owner |
| `repo` | string | Yes | Repository name |
| `first` | int | No | Number of results (default: 10) |
| `category` | string | No | Filter by category slug (e.g., "q-a", "ideas") |
| `answered` | bool | No | Filter by answered status |

**Example:**
```
mcp__github__list_discussions(owner="anthropics", repo="claude-code", category="q-a", answered=False)
```

---

### `mcp__github__get_discussion`

Get full discussion with comments.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `owner` | string | Yes | Repository owner |
| `repo` | string | Yes | Repository name |
| `number` | int | Yes | Discussion number |
| `comment_limit` | int | No | Max comments (default: 50) |
| `comment_sort` | string | No | "upvotes" (default) or "chronological" |

**Example:**
```
mcp__github__get_discussion(owner="anthropics", repo="claude-code", number=123, comment_sort="upvotes")
```

---

## Usage Strategy

### Tool Selection

| Goal | Primary Tool | Secondary |
|------|--------------|-----------|
| Find projects by topic | search_repos | get_repo |
| Find code patterns | search_code | get_file_content |
| Understand structure | get_repo_tree | get_file_content |
| Compare projects | search_repos | get_file_content (README) |
| Find Q&A/help | search_discussions | get_discussion |
| Community insights | list_discussions | get_discussion |

### Reading Priority (per repository)

1. **README.md** - Overview, features, usage
2. **package.json / pyproject.toml** - Dependencies, metadata
3. **docs/ or examples/** - Usage patterns
4. **src/** - Only if critical to answer question

### Result Limits

**search_repos / search_code:**
- Fetch: Top 10-15 results
- Read in depth: Top 3-5
- Skim rest: Only for outliers

**Files per repo:**
- Max 3-4 files (README + key sources)
- Use get_repo_tree first to identify critical files


