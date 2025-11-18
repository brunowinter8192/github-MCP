# Newline Rendering Issue in MCP Tool Responses

**Date:** 2025-11-18 22:44

## Problem

All GitHub MCP server tools displayed literal `\n` escape sequences in Claude Code instead of rendering actual line breaks. Users saw single-line strings like `"Found 39,530 repositories...\n\nTop Results:\n\n1. firecrawl"` instead of properly formatted multi-line output with visible line breaks.

## Root Cause

Claude Code v2.0.22+ introduced undocumented breaking change: when FastMCP tools return primitive `str` types, FastMCP generates both `content` array (TextContent blocks) and `structuredContent` object (JSON). Claude Code v2.0.22+ prioritizes `structuredContent` for display, which shows JSON representation with escaped newlines (`\n`) instead of rendering the `content` array where newlines display correctly. Confirmed in GitHub Issue anthropics/claude-code#9962.

## Fix

Changed all workflow functions to return `list[TextContent]` instead of primitive `str`. This prevents FastMCP from generating `structuredContent`, forcing Claude Code to display only the `content` array where newlines render properly.

**Files modified:**
- src/search_repos.py:5,16-18 - Added TextContent import and wrapper
- src/search_code.py:4,12-14 - Added TextContent import and wrapper
- src/get_repo_tree.py:4,12-17 - Added TextContent import and wrapper
- src/get_file_content.py:5,12-15 - Added TextContent import and wrapper
- server.py:6,27,37,49,59 - Added TextContent import and updated return type annotations
