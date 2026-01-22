# GitHub Tools

FastMCP server providing GitHub search and repository exploration tools.

## search_repos.py

**Purpose:** Search GitHub repositories using the Search API.
**Input:** query string with optional qualifiers, sort_by parameter
**Output:** Human-readable formatted text listing 20 repositories with metadata for direct tree/file access

### search_repos_workflow()
Main orchestrator that coordinates repository search. Calls fetch_repositories to get raw API data, then format_repo_results to extract relevant fields. Returns formatted text string with repository listings.

### fetch_repositories()
Performs HTTP GET request to GitHub Search Repositories API. Constructs URL with query parameters for search term, sort order, and pagination. Sets appropriate headers for API version. Returns raw JSON response.

### format_repo_results()
Transforms raw API response into human-readable text output. Extracts owner, repo name, full_name, description, stars, forks, language, updated_at, and html_url from each repository. Returns formatted text string listing repositories with descriptions, language, stats, and URLs.

## search_code.py

**Purpose:** Search code across GitHub using the Code Search API with text match metadata.
**Input:** query string with search terms and qualifiers
**Output:** Human-readable formatted text listing 20 code matches with repository info and code fragments

### search_code_workflow()
Main orchestrator that coordinates code search. Calls fetch_code_search with text-match header to get highlighted results, then format_code_results to structure the output. Returns formatted text string with code matches and snippets.

### fetch_code_search()
Performs HTTP GET request to GitHub Search Code API. Uses special Accept header to request text-match metadata which provides code fragments. Returns raw JSON response with embedded text_matches arrays.

### format_code_results()
Transforms raw API response into human-readable text output. Extracts repository metadata (owner, repo, full_name, description, stars) and file information (path, file_name, html_url) for each match. Calls extract_text_matches to process code fragments. Returns formatted text string listing code matches with file paths and first three code fragments per match.

### extract_text_matches()
Processes text_matches array from API response. Filters for matches on content and path properties. Returns list of fragment objects showing where search terms appear in the code or file path.

## get_repo_tree.py

**Purpose:** Traverse repository structure with lazy loading to handle large repositories.
**Input:** owner, repo name, optional path for sub-tree exploration
**Output:** Human-readable formatted text showing tree structure with truncation warning if too large

### get_repo_tree_workflow()
Main orchestrator that coordinates tree retrieval. First fetches default branch name, then gets tree SHA for specified path. Fetches full recursive tree and formats response with depth limiting if needed. Returns formatted JSON string with tree items, truncated flag, and optional warning.

### fetch_default_branch()
Gets default branch name for repository by querying repository metadata. Returns branch name string (e.g., "main" or "master").

### get_tree_sha()
Resolves tree SHA for given path. For root path, fetches branch info to get commit tree SHA. For sub-paths, uses Contents API to get directory SHA. Raises ValueError if path is not a directory.

### fetch_tree()
Performs HTTP GET request to GitHub Git Trees API with recursive parameter. Returns complete tree structure with all nested paths flattened into single array. Each item includes path, type (blob/tree), size, and SHA.

### format_tree_response()
Transforms raw tree into human-readable text output. Separates directories and files into categorized lists. Shows up to 50 directories and 50 files. Checks if formatted text exceeds MAX_TREE_CHARS (1000) and appends truncation warning if needed. Returns formatted text string displaying directory path, directories list, and files list with sizes.

## get_file_content.py

**Purpose:** Retrieve and decode file content from GitHub repositories.
**Input:** owner, repo name, file path
**Output:** Human-readable formatted text displaying decoded file content with metadata

### get_file_content_workflow()
Main orchestrator that coordinates file retrieval. Calls fetch_file_content to get raw API response, then format_file_response to decode base64 content. Returns formatted text string with file metadata and decoded content.

### fetch_file_content()
Performs HTTP GET request to GitHub Contents API for specific file path. Returns raw JSON response containing base64-encoded content and metadata.

### format_file_response()
Validates response type is "file" (not directory). Decodes base64 content to UTF-8 string after removing newlines from base64 string. Raises ValueError if path is not a file. Returns formatted text string displaying file metadata (name, path, size, URL) followed by separator and decoded content.

## search_issues.py

**Purpose:** Search GitHub issues using the Search Issues API.
**Input:** query string with optional qualifiers, sort_by parameter
**Output:** Human-readable formatted text listing 20 issues with metadata for direct issue access

### search_issues_workflow()
Main orchestrator that coordinates issue search. Builds query with is:issue qualifier by default, calls fetch_issues to get raw API data, then format_issue_results to extract relevant fields. Returns formatted text string with issue listings.

### build_query()
Adds is:issue qualifier to search query if not already present. Allows explicit is:pr to include pull requests. Returns modified query string.

### fetch_issues()
Performs HTTP GET request to GitHub Search Issues API. Constructs URL with query parameters for search term, sort order, and pagination. Sets appropriate headers for API version. Returns raw JSON response.

### format_issue_results()
Transforms raw API response into human-readable text output. Extracts repository info from repository_url, issue number, title, state, author, comments count, labels, and html_url from each issue. Returns formatted text string listing issues with metadata and tool hints for direct access.

## get_issue.py

**Purpose:** Retrieve full issue details including body content.
**Input:** owner, repo name, issue_number
**Output:** Human-readable formatted text displaying issue with title, metadata, and full body

### get_issue_workflow()
Main orchestrator that coordinates single issue retrieval. Calls fetch_issue to get raw API data, then format_issue to structure the output. Returns formatted text string with complete issue details.

### fetch_issue()
Performs HTTP GET request to GitHub Issues API for specific issue number. Returns raw JSON response containing full issue data including body.

### format_issue()
Transforms raw API response into human-readable text output. Displays title, state, author, dates, labels, comments count, and URL. Includes hint for get_issue_comments if comments exist. Appends full issue body after separator.

## get_issue_comments.py

**Purpose:** Retrieve all comments on a GitHub issue.
**Input:** owner, repo name, issue_number
**Output:** Human-readable formatted text listing all comments with author and content

### get_issue_comments_workflow()
Main orchestrator that coordinates comments retrieval. Calls fetch_comments to get raw API data, then format_comments to structure the output. Returns formatted text string with all comments.

### fetch_comments()
Performs HTTP GET request to GitHub Issue Comments API. Returns array of comment objects with user, body, and created_at fields.

### format_comments()
Transforms raw API response into human-readable text output. Lists total comment count, then each comment with author, date, and full body. Returns formatted text string displaying discussion thread.

## search_prs.py

**Purpose:** Search GitHub pull requests using the Search Issues API with is:pr qualifier.
**Input:** query string with optional qualifiers, sort_by parameter
**Output:** Human-readable formatted text listing 20 PRs with metadata for direct PR access

### search_prs_workflow()
Main orchestrator that coordinates PR search. Builds query with is:pr qualifier, calls fetch_prs to get raw API data, then format_pr_results to extract relevant fields. Returns formatted text string with PR listings.

### build_query()
Adds is:pr qualifier to search query if not already present. Replaces is:issue with is:pr if found. Returns modified query string.

### fetch_prs()
Performs HTTP GET request to GitHub Search Issues API. Constructs URL with query parameters for search term, sort order, and pagination. Returns raw JSON response.

### format_pr_results()
Transforms raw API response into human-readable text output. Extracts repository info, PR number, title, state (including MERGED detection), author, comments count, labels, and html_url. Returns formatted text string with tool hints for direct access.

## list_repo_prs.py

**Purpose:** List pull requests in a specific repository using the Pulls API.
**Input:** owner, repo name, state filter, sort_by parameter
**Output:** Human-readable formatted text listing PRs in the repository with branch info

### list_repo_prs_workflow()
Main orchestrator that coordinates repository PR listing. Calls fetch_repo_prs to get raw API data, then format_pr_list to structure the output. Returns formatted text string with PR list.

### fetch_repo_prs()
Performs HTTP GET request to GitHub Pulls API for repository. Applies state and sort filters. Returns array of PR objects.

### format_pr_list()
Transforms raw API response into human-readable text output. Displays PR number, title, state, author, source and target branches, creation date, labels, and URL. Includes tool hints for get_pr access.

## get_pr.py

**Purpose:** Retrieve full pull request details including body content and statistics.
**Input:** owner, repo name, pull_number
**Output:** Human-readable formatted text displaying PR with title, metadata, stats, and full body

### get_pr_workflow()
Main orchestrator that coordinates single PR retrieval. Calls fetch_pr to get raw API data, then format_pr to structure the output. Returns formatted text string with complete PR details.

### fetch_pr()
Performs HTTP GET request to GitHub Pulls API for specific PR number. Returns raw JSON response containing full PR data including body, commits, additions, deletions.

### format_pr()
Transforms raw API response into human-readable text output. Displays title, state (including MERGED detection), author, branches, dates, merge info, labels, commit count, additions, deletions, changed files count, and mergeable status. Includes hint for get_pr_files. Appends full PR body after separator.

## get_pr_files.py

**Purpose:** Retrieve list of files changed in a pull request.
**Input:** owner, repo name, pull_number
**Output:** Human-readable formatted text listing all changed files with diff statistics

### get_pr_files_workflow()
Main orchestrator that coordinates PR files retrieval. Calls fetch_pr_files to get raw API data, then format_pr_files to structure the output. Returns formatted text string with file list.

### fetch_pr_files()
Performs HTTP GET request to GitHub Pulls Files API. Returns array of file objects with filename, status, additions, deletions, and patch.

### format_pr_files()
Transforms raw API response into human-readable text output. Calculates total additions and deletions. Lists each file with status icon, filename, change counts, and truncated patch preview. Shows renamed files with previous filename.
