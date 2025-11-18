---
description: Run comprehensive CLAUDE.md compliance audit on MCP server project
---

# MCP SERVER COMPLIANCE AUDIT

Systematic compliance review protocol for MCP server projects against CLAUDE.md standards using the specialized compliance-reviewer-mcp agent.

**Execute this command to verify adherence to CLAUDE.md architecture, documentation, and code quality standards.**

---

## CRITICAL RULE

**WHEN IN DOUBT, ASK THE USER.**

If you are uncertain whether a violation should be fixed or is acceptable given project context, ALWAYS ask the user before making changes.

---

## OVERVIEW

This command launches the compliance-reviewer-mcp agent to perform a comprehensive audit of:

- **Architecture patterns** (server.py orchestrator, module structure)
- **Tool parameters** (Annotated + Field, Literal types, docstrings)
- **Documentation structure** (README.md, DOCS.md placement)
- **Critical standards** (comments, emojis, gitignore, fail-fast)
- **Module patterns** (INFRASTRUCTURE → ORCHESTRATOR → FUNCTIONS)
- **Naming conventions** (files, functions, workflows)
- **Error handling** (fail-fast philosophy, proper exceptions)

---

## AGENT INVOCATION

Use the Task tool with subagent_type='compliance-reviewer-mcp' to perform the audit:

```
Task tool parameters:
- subagent_type: 'compliance-reviewer-mcp'
- description: 'CLAUDE.md compliance audit'
- prompt: 'Perform comprehensive compliance audit of this MCP server project against CLAUDE.md standards. Analyze server.py, all src/ modules, configuration files, and documentation. Return detailed report with violations, severity levels, and specific file:line references.'
```

The agent will analyze the entire project and return a structured compliance report.

---

## COMPLIANCE CATEGORIES

### CRITICAL Standards
Violations break the system or fundamentally violate architecture:
- NO comments inside function bodies (only function headers + section markers)
- NO test files in root (ONLY in debug/ folders)
- NO debug/ or logs/ folders in version control (MUST be in .gitignore)
- NO emojis in production code, READMEs, DOCS.md, logs
- server.py MUST be orchestrator only (no business logic)
- Module pattern MUST follow INFRASTRUCTURE → ORCHESTRATOR → FUNCTIONS
- .mcp.json MUST use absolute paths (no relative paths or cwd)
- Fail-fast error handling (no silent error swallowing)

### IMPORTANT Standards
Violations reduce quality but don't break functionality:
- DOCS.md placement (should be in src/domain/, not root)
- Naming conventions (snake_case, _workflow suffix)
- Two-layer documentation (Field descriptions + docstrings)
- Tool separation principle (one tool = one responsibility)
- Proper exception handling (raise_for_status, explicit ValueError)

### RECOMMENDED Standards
Good practices that improve maintainability:
- Type hints on all functions
- Clear function responsibilities
- Proper import organization
- Sensible defaults for optional parameters

---

## RECOMMENDATION FORMAT

After the agent completes the audit, you MUST present recommendations in this format:

```
COMPLIANCE AUDIT SUMMARY:
- Overall Score: XX/100
- Status: PRODUCTION READY / NEEDS FIXES / CRITICAL VIOLATIONS

VIOLATIONS FOUND:
1. [CRITICAL/IMPORTANT/RECOMMENDED] Violation Name
   File: /path/to/file.py:line
   Issue: Brief description
   Standard: Quote from CLAUDE.md
   Fix: What needs to change

2. [SEVERITY] Next violation...

RECOMMENDATIONS:
- CRITICAL fixes (must do): List what must be fixed
- IMPORTANT fixes (should do): List what should be fixed
- RECOMMENDED improvements (optional): List optional improvements

QUESTION (if applicable): [Specific uncertainty about violations or fixes]
RECOMMENDATION: [Your suggested priority - which fixes to tackle first]
REASONING: [Why this priority makes sense for the project]
```

---

## DECISION WORKFLOW

### Step 1: Invoke Agent
Launch compliance-reviewer-mcp agent to perform full audit.

### Step 2: Analyze Report
Review the agent's findings:
- Identify severity levels of all violations
- Note file:line references for each issue
- Understand the standard being violated

### Step 3: Categorize Violations
Group findings by severity:
- **CRITICAL:** Must fix immediately (blocks production use)
- **IMPORTANT:** Should fix soon (reduces quality)
- **RECOMMENDED:** Can fix later (nice-to-have improvements)

### Step 4: Formulate Recommendations
Create actionable recommendations:
- Prioritize CRITICAL fixes first
- Group related violations together
- Suggest implementation order
- Note any contextual exceptions

### Step 5: Present to User
**CRITICAL:** Present recommendations and wait for user decision.

- If violations are clear-cut then Present fix recommendations
- If context matters (e.g., flat structure vs domain folders) then Ask user for guidance
- If uncertain about severity then Ask user to confirm priority

### Step 6: Execute Fixes (if approved)
Only after user approval:
- Fix violations in priority order
- Test after each fix
- Document reasons for any violations left unfixed

---

## COMMON VIOLATIONS AND FIXES

### CRITICAL Violations

**Comments in function bodies:**
```python
# BAD
def workflow():
    data = fetch()  # Get the data
    return format(data)  # Return formatted

# GOOD
def workflow():
    data = fetch()
    return format(data)
```
Fix: Remove all inline comments, keep only function header comments.

**server.py with business logic:**
```python
# BAD
@mcp.tool
def search(query: str):
    response = requests.get(f"{API}/{query}")  # Logic in server.py!
    return response.json()

# GOOD
@mcp.tool
def search(query: str):
    return search_workflow(query)  # Delegate to module
```
Fix: Move all logic to src/ module, keep only delegation in server.py.

**Relative paths in .mcp.json:**
```json
// BAD
{"args": ["run", "server.py"], "cwd": "/path"}

// GOOD
{"args": ["run", "/absolute/path/to/server.py"]}
```
Fix: Convert all paths to absolute, remove cwd field.

### IMPORTANT Violations

**DOCS.md at root instead of src/:**
```
# BAD
project/
├── DOCS.md          # Violates standard
└── src/

# GOOD
project/
└── src/
    └── DOCS.md      # Documentation lives with code
```
Fix: Move DOCS.md to src/ or create domain folders with per-domain DOCS.md.

**Multi-mode tools:**
```python
# BAD
def search(query: str, type: Literal["repos", "code"]):
    if type == "repos": ...
    elif type == "code": ...

# GOOD
def search_repos(query: str): ...
def search_code(query: str): ...
```
Fix: Split into separate tools, one responsibility each.

### RECOMMENDED Improvements

**Missing type hints:**
```python
# BEFORE
def fetch(url):
    return requests.get(url).json()

# AFTER
def fetch(url: str) -> dict:
    return requests.get(url).json()
```
Fix: Add type annotations to all parameters and return values.

---

## EXECUTION CHECKLIST

After running this command, complete the following:

- [ ] Invoke compliance-reviewer-mcp agent via Task tool
- [ ] Review agent's full compliance report
- [ ] Identify all CRITICAL violations (must fix)
- [ ] Identify all IMPORTANT violations (should fix)
- [ ] Note RECOMMENDED improvements (optional)
- [ ] Group related violations together
- [ ] Determine fix priority and order
- [ ] **Formulate recommendations using the format above**
- [ ] **Present recommendations to user:**
  - CRITICAL violations then Recommend immediate fixes
  - IMPORTANT violations then Ask user for priority
  - Context-dependent issues then Ask user for guidance
- [ ] Wait for user approval before making any changes
- [ ] If approved, fix violations in agreed priority order
- [ ] Test after each fix to ensure no regressions
- [ ] Document any violations intentionally left unfixed

---

## EXPECTED AGENT OUTPUT

The compliance-reviewer-mcp agent will return a structured report containing:

1. **Executive Summary**
   - Overall compliance score (0-100)
   - Status assessment
   - Number of violations by severity

2. **Detailed Analysis**
   - Per-category compliance checks
   - File:line references for violations
   - Specific code examples
   - Standard citations from CLAUDE.md

3. **Violation List**
   - Severity level for each issue
   - Affected files and line numbers
   - Description of the problem
   - Required fix

4. **Code Quality Observations**
   - What's done well
   - Areas for improvement
   - Architectural notes

Use this output to formulate your final recommendations to the user.
