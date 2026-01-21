# CLAUDE.MD - MCP Server Engineering Reference

## CRITICAL STANDARDS

- NO comments inside function bodies (only function header comments + section markers)
- NO test files in root (ONLY in debug/ folders - root or per-module)
- NO debug/ or logs/ folders in version control (MUST be in .gitignore)
- NO emojis in production code, READMEs, DOCS.md, logs
- ALWAYS keep script console output concise

**Type hints:** RECOMMENDED but optional

**Fail-Fast:** Let exceptions fly. No try-catch that silently swallows errors affecting business logic. Script must fail if it cannot fulfill its purpose.

---

## server.py (MCP Entry Point)

**Purpose:** MCP server exposing tools to Claude Code. Only imports and tool definitions.

```python
# INFRASTRUCTURE
from typing import Literal
from fastmcp import FastMCP
from dotenv import load_dotenv
from mcp.types import TextContent

load_dotenv()

from src.github.search_repos import search_repos_workflow
from src.github.get_file_content import get_file_content_workflow

mcp = FastMCP("GitHub")


# TOOLS

@mcp.tool
def search_repos(
    query: str,
    sort_by: Literal["stars", "forks", "updated", "best_match"] = "best_match"
) -> list[TextContent]:
    """Search GitHub repositories. Use when user wants to find projects, libraries, or frameworks."""
    return search_repos_workflow(query, sort_by)


@mcp.tool
def get_file_content(owner: str, repo: str, path: str) -> list[TextContent]:
    """Get file content from a repository. Use after browsing repo tree to read specific files."""
    return get_file_content_workflow(owner, repo, path)


if __name__ == "__main__":
    mcp.run()
```

**Rules:**
- NO business logic in server.py
- Each tool delegates to module orchestrator
- Literal for enum-like choices
- Returns list[TextContent] for MCP compatibility

---

## MODULE PATTERN (src/github/tool_name.py)

**CRITICAL:** Each module follows INFRASTRUCTURE -> ORCHESTRATOR -> FUNCTIONS

```python
# INFRASTRUCTURE
import os
import requests
from mcp.types import TextContent

API_BASE = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
RESULTS_LIMIT = 20


# ORCHESTRATOR
def search_repos_workflow(query: str, sort_by: str) -> list[TextContent]:
    raw_data = search_repos_api(query, sort_by)
    return format_response(raw_data)


# FUNCTIONS

# Call GitHub search API
def search_repos_api(query: str, sort_by: str) -> dict:
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    params = {"q": query, "sort": sort_by, "per_page": RESULTS_LIMIT}
    response = requests.get(f"{API_BASE}/search/repositories", headers=headers, params=params)
    response.raise_for_status()
    return response.json()


# Format API response for MCP output
def format_response(data: dict) -> list[TextContent]:
    items = data.get("items", [])
    lines = [f"{r['full_name']} ({r['stargazers_count']} stars)" for r in items]
    return [TextContent(type="text", text="\n".join(lines))]
```

**Section definitions:**

**INFRASTRUCTURE:**
- Imports and constants
- NO functions
- NO logic

**ORCHESTRATOR:**
- ONE function (named: tool_name_workflow)
- Called by server.py tool definition
- Calls internal functions in sequence
- ZERO functional logic (only function composition)

**FUNCTIONS:**
- Ordered by call sequence
- One responsibility each
- Function header comment (one line describing WHAT)
- NO inline comments

---

## TOOL PARAMETER DESIGN

**CRITICAL:** Parameters must be intuitive for LLM understanding

### Two-Layer Documentation (NO DUPLICATION)

**Field Description** = Technical parameter details (what, how, format)
**Docstring** = Semantic use cases (when, why to use this tool)

```python
@mcp.tool
def search_repos(
    query: Annotated[str, Field(description="Search query with GitHub qualifiers (e.g., 'fastapi stars:>1000')")],
    sort_by: Annotated[
        Literal["stars", "forks", "updated", "best_match"],
        Field(description="Sort by: stars (popularity), forks, updated, best_match (relevance)")
    ] = "best_match"
) -> list[TextContent]:
    """Use when user wants to find projects, libraries, or frameworks. Good for discovering alternatives."""
    return search_repos_workflow(query, sort_by)
```

**Field tells LLM:** "How do I fill this parameter?"
**Docstring tells LLM:** "When should I call this tool?"

---

## TOOL OUTPUT DESIGN

**CRITICAL:** Output must be list[TextContent] for MCP compatibility

```python
from mcp.types import TextContent

def format_response(data: dict) -> list[TextContent]:
    text = format_as_string(data)
    return [TextContent(type="text", text=text)]
```

**Principles:**
- Always return list[TextContent]
- Human-readable text format
- Include relevant metadata (stars, dates, etc.)

---

## ERROR HANDLING

**IMPORTANT:** Fail-fast philosophy

**ALLOWED:**
- Retry logic with exponential backoff
- Graceful degradation with explicit logging
- Resource cleanup (connections)

**PROHIBITED:**
- Silently swallowing errors
- Generic `except Exception: pass`
- Hiding failures that affect business logic

```python
response = requests.get(url, headers=headers)
response.raise_for_status()  # Raises on 4xx/5xx
return response.json()
```

FastMCP handles exceptions and communicates errors to client.

---

## DOCUMENTATION STRUCTURE

### Hierarchy

```
github/            -> README.md (setup, env vars, usage)
└── src/github/    -> DOCS.md (module-level docs)
```

**Principle:** README stops where DOCS begins. No redundancy.

---

## CLAUDE CODE INTEGRATION (.mcp.json)

**CRITICAL:** Each MCP server needs .mcp.json for Claude Code registration.

```json
{
  "mcpServers": {
    "github": {
      "command": "/absolute/path/to/venv/bin/fastmcp",
      "args": ["run", "/absolute/path/to/server.py"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Rules:**
- ALL paths MUST be absolute (no relative paths)
- NO cwd field (unreliable in Claude Code)
- Use ${VAR_NAME} syntax for secrets

---

## NAMING CONVENTIONS

**server.py:** Always named server.py
**Domain folder:** src/github/
**Modules:** src/github/search_repos.py, src/github/get_issue.py
**Package markers:** src/__init__.py and src/github/__init__.py
**Orchestrator function:** tool_name_workflow()
**MCP tool function:** @mcp.tool def tool_name()

---

## COMPLIANCE

Scripts in `debug/` folders (root-level or per-module) are exempt from CLAUDE.md compliance requirements.

All other code must follow these standards strictly.
