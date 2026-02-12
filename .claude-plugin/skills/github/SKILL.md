---
name: gh-search
description: GitHub API search and exploration tools
---

# GitHub MCP Tools — Search Strategy

## Navigation Rules

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
  The user has context. Ask for path when genuinely ambiguous, but exhaust cheap self-serve options first:
  1. `get_repo_tree(pattern="*keyword*")` or `grep_repo` to locate files directly
  2. If file found but content doesn't match → **check same directory first** (`depth=1`) for variants (filtered, selected, final, summary...)
  3. If same directory has nothing → broaden scope one level up
  4. Only after 2-3 failed attempts → ask user
  Use existing context (beads, conversation history) as navigation hints.

- **Exploratory search** (discover trends, compare repos, survey landscape):
  The user has no specific target. Navigate freely with tools.
  Drill down via get_repo_tree, read READMEs, follow interesting leads.
  Example: "What are hot topics in Claude Code?" → Browse repos, read discussions.

**5. Filename search before content search.**
When looking for a specific example or report, search by the broadest known identifier in the filename FIRST (e.g., template name, query ID), not by specific content details (e.g., node IDs, exact values).
- `get_repo_tree(pattern="*Q8*", path="Predictions/")` → finds all Q8 reports in one call
- `grep_repo(pattern="13408", file_pattern="*.md")` → may miss due to `max_files` limit
Also: when using `grep_repo` on directories with many files, increase `max_files` beyond the default 10.

**6. Truncation → spawn subagent.**
When `grep_repo` or `get_repo_tree` returns a truncation warning, do NOT repeat with same scope.
Instead: spawn a `github-search` subagent to search the truncated directory.
The subagent can independently narrow scope by drilling into subdirectories.
Example: `grep_repo(path="Dynamic")` truncated → spawn subagent:
"Search for value 48.5 in CSV files under Prediction_Methods/Dynamic/Runtime_Prediction.
Drill into subdirectories with depth=1 first, then grep_repo with narrow path."

**Detection:** If the user references specific data (table, number, file, claim) → targeted.
If the user says "look around", "explore", "what's out there" → exploratory.

## Subagent Dispatch (github-search)

| Agent | subagent_type | Model | Output |
|-------|---------------|-------|--------|
| github-search | `github-search` | Haiku | Repos with file paths |

**Usage:** `Task(subagent_type="github-search", prompt="...")`

### When to Use

- Finding repos by topic/technology
- Searching code patterns across GitHub
- Comparing multiple repos for a use case
- Investigating issues/PRs in unknown repos
- **API truncation** on large repos — agent can independently narrow scope and drill into subdirectories

### When NOT to Use

- You know the exact repo (use MCP tools directly)
- Single file lookup in known repo
- Simple targeted search where 1-2 tool calls suffice

### How to Prompt

**BAD:**
- "Find semantic search repos" (too vague)
- "Search vector databases" (no scope)

**GOOD:**
- "Find 3-5 Python repos for semantic search, stars >500"
- "Search for FastMCP + embedding patterns, return implementation paths"
- "Search for value 48.5 in CSV files under Prediction_Methods/Dynamic/Runtime_Prediction. Drill into subdirectories with depth=1 first, then grep_repo with narrow path."

**Template:**
```
Research [TOPIC] on GitHub.

Focus on:
1. [Specific aspect 1]
2. [Specific aspect 2]

For each repo found:
- Name, stars, description
- Key implementation files (paths!)
- [Specific evaluation criteria]
```

**Truncation Template:**
```
Search for [VALUE/PATTERN] in [REPO] under [TRUNCATED_PATH].

Strategy:
1. get_repo_tree(path="[TRUNCATED_PATH]", depth=1) to discover subdirectories
2. grep_repo with narrow path on each subdirectory
3. Report all matches with full file paths
```

### After Agent Returns

**Agent = Scout with Paths**

Agent provides:
- WHERE: Repo + file paths
- WHAT: Summary of capabilities

**You can:**
1. Present results directly to user
2. For detail questions: `get_file_content` with provided paths
3. Paths are verified (from `get_repo_tree` output)

**Verification:**
- [ ] Check at least 1 repo exists
- [ ] Confirm file paths look valid
- [ ] If agent provided summary: spot-check 1-2 details

### Known Pitfalls (Haiku)

1. **Missing Paths** — Agent may forget file paths. Fix: Explicitly ask "Include key implementation file paths"
2. **Format Drift** — Agent uses own format instead of requested. Fix: Say "Use EXACTLY this format:" with template
3. **Local Path Leak** — Agent may include local filesystem paths. Fix: Verify output contains only GitHub paths

## Tool Selection

| Goal | Primary Tool | Secondary |
|------|--------------|-----------|
| Find projects by topic | search_repos | get_repo |
| Find code patterns | search_code | get_file_content |
| Understand structure | get_repo_tree | get_file_content |
| Compare projects | search_repos | get_file_content (README) |
| Find Q&A/help | search_discussions | get_discussion |
| Community insights | list_discussions | get_discussion |

## Reading Priority (per repository)

1. **README.md** - Overview, features, usage
2. **package.json / pyproject.toml** - Dependencies, metadata
3. **docs/ or examples/** - Usage patterns
4. **src/** - Only if critical to answer question

## Result Limits

**search_repos / search_code:**
- Fetch: Top 10-15 results
- Read in depth: Top 3-5
- Skim rest: Only for outliers

**Files per repo:**
- Max 3-4 files (README + key sources)
- Use get_repo_tree first to identify critical files

## Known Limitations

**`get_repo_tree` — truncation warning on large repos (Issue #1):**
- GitHub Git Trees API truncates at ~100k entries
- Tool now warns when `truncated=true` in API response
- **Workaround:** Use `path` parameter to narrow search scope — smaller subtree avoids truncation

**`search_code` — does not index CSV/data files (Issue #2):**
- GitHub Code Search skips `type: data` files (CSV, TSV, etc. per GitHub Linguist)
- Tool now shows a NOTE when 0 results, suggesting `grep_file` or `grep_repo`
- **Fallback:** `grep_repo` searches file content across repo by file pattern

**Data files in large repos:**
- Use `grep_repo(pattern="search_term", file_pattern="*.csv", path="subdir")` for content search in data files
- `grep_repo` combines `get_repo_tree(pattern=...)` + `grep_file` automatically

## Searching for Values

When searching for numeric values in CSVs or data files:
- **Stored format ≠ display format:** 6.74% is stored as `0.06741992...`
- `search_code("6.74")` → 0 results. `search_code("0.0674")` → may also fail (CSV not indexed)
- **Strategy:** Search for the column/metric name (e.g., `overall_mre`) instead of the value itself
- **Best approach for data files:** `grep_repo` to search content across matching files
