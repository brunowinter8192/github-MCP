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
| `mcp__github__get_file_content` | Read file contents from a repo (supports offset/limit for line ranges) |
| `mcp__github__grep_file` | Search file content by regex pattern |
| `mcp__github__search_repo_files` | Find files by name pattern (glob) |
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
| `metadata_only` | bool | No | If true, return only file metadata (name, size, type, SHA, URL) without content. Use to check file existence or size without downloading. Default: false |
| `offset` | int | No | Start line (0-based, default: 0). Use with limit for line range reading |
| `limit` | int | No | Number of lines to return (default: 0 = all lines). Use to read specific portions of large files |

**Example:**
```
mcp__github__get_file_content(owner="fastmcp", repo="fastmcp", path="README.md")
mcp__github__get_file_content(owner="user", repo="repo", path="large_file.csv", metadata_only=True)
mcp__github__get_file_content(owner="user", repo="repo", path="data.csv", offset=0, limit=10)
```

---

### `mcp__github__grep_file`

Search file content by regex pattern. Returns matching lines with line numbers.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `owner` | string | Yes | Repository owner |
| `repo` | string | Yes | Repository name |
| `path` | string | Yes | File path to search in |
| `pattern` | string | Yes | Regex pattern to match against each line |
| `context_lines` | int | No | Lines of context before/after each match (like grep -C). Default: 0 |
| `max_matches` | int | No | Maximum number of matches to return. Default: 50 |

**Example:**
```
mcp__github__grep_file(owner="user", repo="repo", path="data.csv", pattern="Q13.*?;0;")
mcp__github__grep_file(owner="user", repo="repo", path="config.py", pattern="API_KEY", context_lines=2)
```

---

### `mcp__github__search_repo_files`

Find files by name pattern (glob) in a repository.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `owner` | string | Yes | Repository owner |
| `repo` | string | Yes | Repository name |
| `pattern` | string | Yes | Glob pattern to match filenames (e.g., "*.csv", "*runtime*"). Matches against basename by default; use "/" in pattern to match full path |
| `path` | string | No | Subdirectory to search within (default: entire repo) |

**Example:**
```
mcp__github__search_repo_files(owner="user", repo="repo", pattern="*histograms*")
mcp__github__search_repo_files(owner="user", repo="repo", pattern="*.csv", path="data")
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

### Navigation Rules

**1. DOCS first — always.**
Before opening data files or CSVs in any directory, check for README.md or DOCS.md in that directory (or parent). Well-documented repos explain which files are authoritative and what each subdirectory contains. Skipping DOCS leads to reading the wrong file.

**2. Ambiguous matches — check all, report discrepancy.**
When multiple files share the same name in different paths (e.g., `two_step_evaluation_overview.csv` in both `Misc/` and `Prediction_Methods/`): read both, compare values, and report which matches and which doesn't. Never silently pick one and assume it's correct.

**3. When unsure — show both to the user.**
If you cannot determine which source is authoritative, present both findings with their full paths and let the user decide. One wrong assumption wastes more time than one extra tool call.

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

### Known Limitations

**`search_repo_files` — silent truncation on large repos (Issue #1):**
- GitHub Git Trees API truncates at ~100k entries without error
- On large repos (>10k files), `search_repo_files` may silently miss files
- **Workaround:** Use `path` parameter to narrow search scope (e.g., `search_repo_files(pattern="*.md", path="src/module")`) — smaller subtree avoids truncation
- **Fallback:** Use `search_code("filename repo:owner/repo")` — uses GitHub Code Search index, no truncation

**`search_code` — does not index CSV/data files (Issue #2):**
- GitHub Code Search skips certain file types (CSVs, data files, possibly generated files)
- Searching for CSV column headers or values returns 0 results even when content exists
- **Fallback:** Navigate via `get_repo_tree` → then `grep_file` on specific files

**Combined gap:** For data files in large repos, neither `search_repo_files` nor `search_code` is reliable. Use `get_repo_tree` (with `depth=1`, drilling down step by step) + `grep_file` as the safe path. See Issue #3 for API investigation.

### Searching for Values

When searching for numeric values in CSVs or data files:
- **Stored format ≠ display format:** 6.74% is stored as `0.06741992...`
- `search_code("6.74")` → 0 results. `search_code("0.0674")` → may also fail (CSV not indexed)
- **Strategy:** Search for the column/metric name (e.g., `overall_mre`) instead of the value itself
- **Best approach for data files:** `get_repo_tree` to find CSVs → `grep_file` to search content


