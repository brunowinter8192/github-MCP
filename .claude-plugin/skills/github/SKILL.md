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
| `mcp__github__grep_repo` | Search file content across repo by file pattern |
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

### `mcp__github__grep_repo`

Search file content across a repository by file name pattern. Combines `search_repo_files` (find files by glob) + `grep_file` (search content by regex). Use when `search_code` fails on data files (CSV, TSV, etc.).

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `owner` | string | Yes | Repository owner |
| `repo` | string | Yes | Repository name |
| `pattern` | string | Yes | Regex pattern to match against file content |
| `file_pattern` | string | No | Glob pattern for file names (default: "*.csv") |
| `path` | string | No | Subdirectory to scope search (default: repo root) |
| `max_files` | int | No | Max files to search (default: 10, protects API rate) |

**Note:** `max_files` limits how many files are searched (not found). If more files match the glob than `max_files`, the rest are skipped. Use `path` to narrow scope or increase `max_files` for complete results.

**Example:**
```
mcp__github__grep_repo(owner="user", repo="repo", pattern="mean_actual_ms", file_pattern="*summary*", path="Evaluation")
mcp__github__grep_repo(owner="user", repo="repo", pattern="def.*workflow", file_pattern="*.py")
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

**2. Ambiguous matches — check ALL before reporting.**
When multiple candidates exist (same filename in different paths, multiple subdirectories like `approach_1/` through `approach_4/`, different versions of the same data): check ALL of them BEFORE reporting any result to the user. Never report a mismatch after checking only one candidate when others remain unchecked. The correct workflow is:
1. Identify all candidates (parallel `get_file_content` or `grep_file` calls)
2. Compare each against the expected data
3. Report the full picture: which matches, which don't, and why

**Bad:** "v2/config.json doesn't match. Should I check the others?"
**Good:** "Found config.json in 3 locations. v1/ matches the expected data, v2/ and v3/ differ because [reasons]."

**3. When no candidate matches — show all to the user.**
If after checking ALL candidates none matches, present all findings with their full paths and let the user decide. One wrong assumption wastes more time than a few extra tool calls.

**4. Search Mode — targeted vs exploratory.**

Two fundamentally different search modes exist:

- **Targeted search** (user asked for specific data, verification, comparison):
  The user has context. ALWAYS ask the user for the concrete path/location FIRST.
  Max 2-3 exploratory tool calls if path is ambiguous, then ask.
  Use existing context (beads, conversation history) as navigation hints.
  Example: "Verify Table 5.2 numbers" → Ask "Which directory?" before navigating.

- **Exploratory search** (discover trends, compare repos, survey landscape):
  The user has no specific target. Navigate freely with tools.
  Drill down via get_repo_tree, read READMEs, follow interesting leads.
  Example: "What are hot topics in Claude Code?" → Browse repos, read discussions.

**Detection:** If the user references specific data (table, number, file, claim) → targeted.
If the user says "look around", "explore", "what's out there" → exploratory.

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

**`search_repo_files` — truncation warning on large repos (Issue #1):**
- GitHub Git Trees API truncates at ~100k entries
- Tool now warns when `truncated=true` in API response
- **Workaround:** Use `path` parameter to narrow search scope — smaller subtree avoids truncation

**`search_code` — does not index CSV/data files (Issue #2):**
- GitHub Code Search skips `type: data` files (CSV, TSV, etc. per GitHub Linguist)
- Tool now shows a NOTE when 0 results, suggesting `grep_file` or `grep_repo`
- **Fallback:** `grep_repo` searches file content across repo by file pattern

**Data files in large repos:**
- Use `grep_repo(pattern="search_term", file_pattern="*.csv", path="subdir")` for content search in data files
- `grep_repo` combines `search_repo_files` + `grep_file` automatically

### Searching for Values

When searching for numeric values in CSVs or data files:
- **Stored format ≠ display format:** 6.74% is stored as `0.06741992...`
- `search_code("6.74")` → 0 results. `search_code("0.0674")` → may also fail (CSV not indexed)
- **Strategy:** Search for the column/metric name (e.g., `overall_mre`) instead of the value itself
- **Best approach for data files:** `grep_repo` to search content across matching files


