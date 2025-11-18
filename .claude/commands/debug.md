---
description: Systematic debugging with context gathering, debug-specialist subagent and bug documentation
argument-hint: [observation/error-description]
---

## Problem Observation

User observes: $ARGUMENTS

---

## Phase 1: Context Gathering

**CRITICAL:**
- Read the codebase BROADLY to understand the user's problem and effectively prompt the subagent
- If unclear what the user means, ask clarifying questions before prompting the subagent

1. Identify affected modules based on the observation
2. Check bug_fixes/ in root to see if such an issue existed before, it's possible the issue was previously fixed but reappeared due to a new feature
3. Find relevant files in the codebase (max 3-4, focused)
4. Check `logs/` folder if present
5. Determine debug/ location: root-level (simple MCP) or src/[module]/debug/ (complex MCP)
6. Gather: Error messages, stack traces, affected functions with File:Line references

---

## Phase 2: Parallel Multi-Agent Debug

**CRITICAL:** Launch 3 debug-specialist agents in parallel to get multiple perspectives.

**MANDATORY:** Each agent gets its own isolated workspace:
- Agent 1 → `debug/Agent_1/`
- Agent 2 → `debug/Agent_2/`
- Agent 3 → `debug/Agent_3/`

Call 3 Task tools **in a single message** (parallel execution):

```json
{
  "tool": "Task",
  "parameters": {
    "description": "debug issue (Agent 1)",
    "subagent_type": "debug-specialist",
    "prompt": "## Problem Description\n<Precise description of what is failing, expected vs actual behavior>\n\n## Investigation Results\n<Findings from Phase 1: error messages, stack traces, affected functions with File:Line references>\n\n## Recommended Starting Points\n<Specific folders and files the subagent should examine first, ordered by relevance>\n\n## CRITICAL: Workspace\nYou MUST create all debug scripts and test files in: debug/Agent_1/\nThis is YOUR isolated workspace. Other agents work in Agent_2/ and Agent_3/."
  }
}
```

Repeat for Agent 2 and Agent 3 with their respective workspace paths.

---

## Phase 2.4: Assess Agent Debug Plans

**CRITICAL:** Agents deliver their debug plans BEFORE executing Step 2 (Reproduce).

After Phase 2 agents return with their initial reports, assess their planned approaches:

### Collect Agent Plans

Each agent provides:
1. **Root Cause Analysis** - What they identified as the problem source
2. **Debug Plan** - What they intend to test/reproduce
3. **Planned Scripts** - Which debug scripts they will create

### Assessment Criteria

1. **Root Cause Consensus**
   - Do all 3 agents identify the same root cause?
   - If NO: Which agent has the most credible analysis?

2. **Approach Overlap**
   - Are agents planning to test identical approaches?
   - If YES: Redirect agents to test different solutions

3. **Plan Quality**
   - Is the debug plan comprehensive?
   - Does it cover reproduction + validation?
   - Are planned scripts well-structured?

4. **Approach Diversity**
   - Do agents cover different solution strategies?
   - If NO: Assign specific alternative approaches to ensure diversity

### Decision & Recommendation Format

For each agent, document:

```
AGENT [X] ASSESSMENT
====================

Root Cause: [Agent's identified root cause]
Planned Approach: [Brief summary of debug plan]
Planned Scripts: [List of scripts agent will create]

OVERLAP CHECK:
- With Agent Y: [HIGH/MEDIUM/LOW overlap - explain]
- With Agent Z: [HIGH/MEDIUM/LOW overlap - explain]

QUALITY: [EXCELLENT/GOOD/NEEDS_IMPROVEMENT - explain]

DECISION: GO / REDIRECT / MERGE
REASONING: [Why this decision]

INSTRUCTIONS TO AGENT:
[If GO: "Proceed with your planned approach"]
[If REDIRECT: "Focus on [specific alternative approach] instead because [reason]"]
[If MERGE: "Collaborate with Agent Y to test [combined approach]"]
```

### Overall Recommendation

After assessing all 3 agents:

```
OVERALL ASSESSMENT
==================

Root Cause Consensus: YES/NO - [explanation]
Approach Diversity: EXCELLENT/GOOD/POOR - [explanation]

AGENTS TO PROCEED:
- Agent 1: [GO/REDIRECT/MERGE] - [brief instruction]
- Agent 2: [GO/REDIRECT/MERGE] - [brief instruction]
- Agent 3: [GO/REDIRECT/MERGE] - [brief instruction]

EXPECTED OUTCOME:
[What solutions/validations you expect from the 3 agents after redirection]
```

### Send Continuation Instructions

Resume each agent with specific instructions based on decisions above. Agents continue from Step 2 (Reproduce) with their assigned approach.

---

## Phase 2.5: Agent Results Aggregation

After all 3 agents complete, analyze their solutions:

### Comparison Criteria
1. **Consensus Check**: Do all 3 agents identify the same root cause?
2. **Solution Diversity**: How different are the proposed fixes?
3. **Test Quality**: Which agent wrote the most comprehensive debug scripts?
4. **Root Cause Analysis**: Which agent went deepest in identifying the issue?
5. **CLAUDE.md Compliance**: Which solution follows standards best?

### Assessment Output
Present to yourself (before showing user):

```
AGENT COMPARISON REPORT
=======================

Root Cause Consensus:
- Agent 1: [brief summary]
- Agent 2: [brief summary]
- Agent 3: [brief summary]
- Consensus: [YES/NO - explain]

Proposed Solutions:
- Agent 1: [approach summary]
- Agent 2: [approach summary]
- Agent 3: [approach summary]

Test Coverage:
- Agent 1: [files created, test comprehensiveness]
- Agent 2: [files created, test comprehensiveness]
- Agent 3: [files created, test comprehensiveness]

RECOMMENDED SOLUTION: Agent [X]
REASONING: [Why this solution is best - consider all criteria above]

REJECTED SOLUTIONS:
- Agent [Y]: [Why rejected or inferior]
- Agent [Z]: [Why rejected or inferior]
```

---

## Phase 3: Present Multi-Agent Analysis to User

After completing Phase 2.5 aggregation:

1. **Show the Agent Comparison Report** (from Phase 2.5)
2. **Present your recommended solution** with clear reasoning
3. **Highlight key differences** between the 3 approaches
4. **Show consensus areas** (if all agents agreed on root cause)
5. **WAIT for explicit user confirmation** before proceeding
6. Ask: "Should I implement the recommended fix from Agent [X]?"

**IMPORTANT:** User might choose a different agent's solution than your recommendation. Be prepared to implement their choice.

---

## Phase 4: Implementation and Documentation (after Approval)

### 4.1 Implement Fix
- Apply the proposed fix
- Test the changes

### 4.2 Document Bug Fix
**Location:** `bug_fixes/` (in project root)

**Filename:** `[descriptive-name]_YYYYMMDD_HHMMSS.md`

**Format (CONCISE):**
```markdown
# [Short Bug Title]

**Date:** YYYY-MM-DD HH:MM

## Problem
[How the problem manifested - 2-3 sentences max]

## Root Cause
[What was the root cause - 2-3 sentences max]

## Fix
[How it was fixed - File:Line references]
```

**IMPORTANT:** Documentation must be short and concise - no prose, only facts.
