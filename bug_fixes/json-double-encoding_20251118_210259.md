# JSON Double-Encoding Output Issue

**Date:** 2025-11-18 21:02

## Problem
GitHub MCP server returned JSON-escaped gibberish instead of clean human-readable output. Users saw escaped quotes and newlines like `{"result":"{\n  \"total_count\": 119429,\n  \"items\": [\n ..."}` making the output unreadable. Context7 MCP displayed clean formatted text, but GitHub MCP did not.

## Root Cause
All 4 format functions used `json.dumps(result, indent=2)` which created JSON strings. When FastMCP serialized these tool responses for the MCP protocol, it wrapped the already-JSON string in another JSON layer, causing double-encoding where inner quotes became `\"` and newlines became `\n`.

## Fix
Replaced `json.dumps()` with human-readable text formatters in all 4 modules:
- src/search_repos.py:50-78 - Returns "Found X repositories" + numbered list
- src/search_code.py:39-73 - Returns "Found X code matches" + file paths with fragments
- src/get_file_content.py:35-64 - Returns file metadata + separator + content
- src/get_repo_tree.py:75-102 - Returns directories/files categorized lists

Removed `import json` from all 4 modules (kept `import base64` in get_file_content.py for decoding).
