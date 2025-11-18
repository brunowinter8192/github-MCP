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
