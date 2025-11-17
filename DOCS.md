# GitHub MCP Server
FastMCP server providing GitHub search and repository exploration tools.

## Project Structure
```
github/
├── server.py              # FastMCP server entry point
├── src/                   # Tool modules
│   ├── __init__.py        # Package marker
│   ├── search_repos.py    # Repository search module
│   ├── search_code.py     # Code search module
│   ├── get_repo_tree.py   # Repository tree traversal module
│   └── get_file_content.py # File content retrieval module
├── DOCS.md                # This documentation
├── README.md              # Quick start guide
├── .mcp.json              # Claude Code MCP registration
└── debug/                 # Test scripts (gitignored)
```

## server.py
**Purpose:** MCP server orchestrator that imports and exposes tools from all modules.

### search_repos()
Searches GitHub repositories by keywords and qualifiers. Delegates to search_repos_workflow. Returns repositories matching the query with metadata including owner, repo name, description, stars, forks, language, and update timestamp.

### search_code()
Searches code across GitHub repositories. Delegates to search_code_workflow. Returns code matches with text fragments showing where search terms appear, plus repository metadata for direct file access.

### get_repo_tree()
Gets repository file tree structure with lazy loading. Delegates to get_repo_tree_workflow. Returns tree items limited to depth 0 and 1 if response exceeds 1000 characters, with warning message for truncated results.

### get_file_content()
Gets content of a specific file from repository. Delegates to get_file_content_workflow. Returns decoded file content with metadata including name, path, size, and SHA.

## src/search_repos.py
**Purpose:** Search GitHub repositories using the Search API.
**Input:** query string with optional qualifiers, sort_by parameter
**Output:** List of 20 repositories with metadata for direct tree/file access

### search_repos_workflow()
Main orchestrator that coordinates repository search. Calls fetch_repositories to get raw API data, then format_repo_results to extract relevant fields. Returns structured dictionary with total_count and items array.

### fetch_repositories()
Performs HTTP GET request to GitHub Search Repositories API. Constructs URL with query parameters for search term, sort order, and pagination. Sets appropriate headers for API version. Returns raw JSON response.

### format_repo_results()
Transforms raw API response into clean output structure. Extracts owner, repo name, full_name, description, stars, forks, language, updated_at, and html_url from each repository. Returns dictionary with total_count and formatted items array.

## src/search_code.py
**Purpose:** Search code across GitHub using the Code Search API with text match metadata.
**Input:** query string with search terms and qualifiers
**Output:** List of 20 code matches with repository info and code fragments

### search_code_workflow()
Main orchestrator that coordinates code search. Calls fetch_code_search with text-match header to get highlighted results, then format_code_results to structure the output. Returns dictionary with total_count and items containing both repo metadata and code snippets.

### fetch_code_search()
Performs HTTP GET request to GitHub Search Code API. Uses special Accept header to request text-match metadata which provides code fragments. Returns raw JSON response with embedded text_matches arrays.

### format_code_results()
Transforms raw API response into structured output. Extracts repository metadata (owner, repo, full_name, description, stars) and file information (path, file_name, html_url) for each match. Calls extract_text_matches to process code fragments. Returns dictionary with total_count and formatted items.

### extract_text_matches()
Processes text_matches array from API response. Filters for matches on content and path properties. Returns list of fragment objects showing where search terms appear in the code or file path.

## src/get_repo_tree.py
**Purpose:** Traverse repository structure with lazy loading to handle large repositories.
**Input:** owner, repo name, optional path for sub-tree exploration
**Output:** Tree structure with truncation warning if too large

### get_repo_tree_workflow()
Main orchestrator that coordinates tree retrieval. First fetches default branch name, then gets tree SHA for specified path. Fetches full recursive tree and formats response with depth limiting if needed. Returns dictionary with tree items, truncated flag, and optional warning.

### fetch_default_branch()
Gets default branch name for repository by querying repository metadata. Returns branch name string (e.g., "main" or "master").

### get_tree_sha()
Resolves tree SHA for given path. For root path, fetches branch info to get commit tree SHA. For sub-paths, uses Contents API to get directory SHA. Raises ValueError if path is not a directory.

### fetch_tree()
Performs HTTP GET request to GitHub Git Trees API with recursive parameter. Returns complete tree structure with all nested paths flattened into single array. Each item includes path, type (blob/tree), size, and SHA.

### format_tree_response()
Transforms raw tree into output format. Converts type "tree" to "dir" and "blob" to "file" for clarity. Checks if formatted tree exceeds MAX_TREE_CHARS (1000). If exceeded, filters to depth 0 and 1 only and sets warning message. Returns dictionary with base_path, tree items, truncated flag, and warning.

### filter_by_depth()
Filters tree items by path depth. Counts slashes in path to determine depth. Returns only items where depth is less than or equal to max_depth parameter.

## src/get_file_content.py
**Purpose:** Retrieve and decode file content from GitHub repositories.
**Input:** owner, repo name, file path
**Output:** Decoded file content with metadata

### get_file_content_workflow()
Main orchestrator that coordinates file retrieval. Calls fetch_file_content to get raw API response, then format_file_response to decode base64 content. Returns dictionary with file name, path, size, decoded content, SHA, and HTML URL.

### fetch_file_content()
Performs HTTP GET request to GitHub Contents API for specific file path. Returns raw JSON response containing base64-encoded content and metadata.

### format_file_response()
Validates response type is "file" (not directory). Decodes base64 content to UTF-8 string after removing newlines from base64 string. Raises ValueError if path is not a file. Returns dictionary with name, path, size, decoded content, sha, and html_url.
