---
name: jf-new-project
description: Initialize new JueFlow project: questions → research → requirements → roadmap.
tools: Read, Write, Bash, Exec
color: purple
---

<objective>
Initialize a new project with full JueFlow context:
1. Ask questions until project is fully understood
2. Spawn Project Researcher to survey domain
3. Extract requirements (v1, v2, out of scope)
4. Create roadmap with phases mapped to requirements
5. Get user approval

Creates: PROJECT.md, REQUIREMENTS.md, ROADMAP.md, STATE.md, research/
</objective>

<process>

## Stage 1: Project Questions

Ask until you understand:

### Vision & Goals
- What is this project? (Brief description)
- What problem does it solve? (For whom?)
- What's the core value proposition?
- Success criteria: How do we know it works?

### Technical Constraints
- Any specific stack preferences or restrictions?
- Deployment target (local, Vercel, custom)?
- Performance requirements?
- Security requirements?

### Timeline & Scope
- Is this MVP, v1, or larger?
- Rough timeline (weeks/months)?
- Must-have vs nice-to-have features?

### Preferences
- Style preferences (minimal, expressive, industrial, playful)?
- UI/UX philosophy opinionated or flexible?
- Testing approach (manual, automated, minimal, comprehensive)?

**Stop when:** You have enough context to define clear project boundaries.

</process>

## Stage 2: Spawn Project Researcher

```bash
cd /root/clawd
jue sessions_spawn -task "Analyze domain ecosystem for project: @input.project_description" -agent main -label jf-project-researcher -timeout 600
```

**Wait for research agent to complete.**

**Researcher outputs:** `research/SUMMARY.md`, `research/STACK.md`, `research/FEATURES.md`, `research/ARCHITECTURE.md`, `research/PITFALLS.md`

**Load these files.** Use them to inform requirements and roadmap.

</process>

## Stage 3: Extract Requirements

Create `REQUIREMENTS.md`:

```markdown
# Project Requirements

## Project Overview
[Description from questions]

## Success Criteria
- [Criteria 1]
- [Criteria 2]
- [Criteria 3]

## Technical Constraints
- [Constraint 1]
- [Constraint 2]

## Scope Definition

### Must-Have (v1)
| Feature | Why Required | Priority |
|---------|---------------|----------|
| [Feature A] | | High |
| [Feature B] | | High |

### Nice-to-Have (v2)
| Feature | Why Nice-to-Have | Priority |
|---------|-------------------|----------|
| [Feature X] | | Medium |
| [Feature Y] | | Low |

### Out of Scope
| Feature | Why Out of Scope | Maybe Later? |
|---------|------------------|---------------|
| [Feature Z] | Too complex for v1 | v2 |
| [Feature W] | Not core value proposition | v3 |
```

**Requirements traceability:** Each feature should map to a phase in roadmap.

</process>

## Stage 4: Create Roadmap

Create `ROADMAP.md`:

```markdown
# Project Roadmap

## Milestone: v1

### Phase 1: [Phase Name]
**Goal:** [What this phase achieves]
**Must-haves:** [List of features]
**Estimated complexity:** Low|Medium|High
**Dependencies:** None

### Phase 2: [Phase Name]
**Goal:** [What this phase achieves]
**Must-haves:** [List of features]
**Estimated complexity:** Low|Medium|High
**Dependencies:** Phase 1

### Phase 3: [Phase Name]
**Goal:** [What this phase achieves]
**Must-haves:** [List of features]
**Estimated complexity:** Low|Medium|High
**Dependencies:** Phase 2

## Milestone: v2 (Future)
[Placeholder for future milestones]

## Progress Tracking

| Phase | Status | Started | Completed | Notes |
|-------|--------|---------|-----------|
| 1 | Not Started | - | - |
| 2 | Not Started | - | - |
| 3 | Not Started | - | - |
```

**Use research findings to:**
- Structure phases logically (ARCHITECTURE.md recommendations)
- Order phases by dependency (SUMMARY.md recommendations)
- Set reasonable complexity estimates (PITFALLS.md warnings)

</process>

## Stage 5: Get User Approval

Present roadmap to user:

```
🎯 Project: [Project Name]

📋 v1 Scope: [3-5 bullet summary of must-haves]

🗺 Roadmap (v1):
1. Phase 1 - [Name]: [1-line goal]
2. Phase 2 - [Name]: [1-line goal]
3. Phase 3 - [Name]: [1-line goal]

🔧 Tech Stack (from research):
- Frontend: [Stack]
- Backend: [Stack]
- Database: [Stack]

✅ Approve this roadmap?
- "Yes, let's go"
- "Adjust phase N" - iterate on specific phase
- "Add feature X to v1" - modify requirements
- "Start over" - scrap and restart questions
```

**If approved:**
1. Create `STATE.md` with initial state
2. Set all phases to "Not Started"
3. Ready to proceed with `/jf:discuss-phase 1`

**If adjustments requested:**
1. Iterate on requirements/roadmap
2. Re-present for approval
3. Loop until approved

</process>

<file_structure>

## Files Created

```
.planning/
├── PROJECT.md           # Project vision, goals, success criteria
├── REQUIREMENTS.md     # Must-haves, nice-to-haves, out of scope
├── ROADMAP.md          # Phases, milestones, progress tracking
├── STATE.md            # Initial state (phase status, blockers)
└── research/           # Created by Project Researcher
    ├── SUMMARY.md
    ├── STACK.md
    ├── FEATURES.md
    ├── ARCHITECTURE.md
    └── PITFALLS.md
```

### PROJECT.md
```markdown
# [Project Name]

## Vision
[One-sentence vision statement]

## Goals
- [Goal 1]
- [Goal 2]
- [Goal 3]

## Success Criteria
This project is successful when:
- [Criteria 1]
- [Criteria 2]

## Constraints
- Technical: [List]
- Time: [Timeline]
- Resources: [Available resources]

## Context
Always load this file for project context.
It contains the North Star - why we're building this.
```

### STATE.md
```markdown
# Project State

Last Updated: [Timestamp]

## Current Phase
Phase [N] - [Phase Name]

## Phase Status

| Phase | Name | Status | Started | Completed | Blockers |
|-------|------|--------|---------|----------|
| 1 | [Name] | Not Started | - | None |
| 2 | [Name] | Not Started | - | None |
| 3 | [Name] | Not Started | - | None |

## Decisions Log
- [Date] - [Decision] - Reason: [Why]
- [Date] - [Decision] - Reason: [Why]

## Blockers
None currently

## Notes
[Additional context between sessions]
```
</file_structure>

<return>

## Return to User

After approval, return:

```markdown
✅ **Project Initialized: [Project Name]**

📁 Files Created:
- PROJECT.md - Project vision and goals
- REQUIREMENTS.md - v1/v2 scope definition
- ROADMAP.md - Phase-by-phase build plan
- STATE.md - Current progress tracking
- research/ - Domain ecosystem research

🚀 **Next Steps:**
1. `/jf:discuss-phase 1` - Shape Phase 1 implementation
2. `/jf:plan-phase 1` - Create task plans
3. `/jf:execute-phase 1` - Build it autonomously
4. `/jf:verify-work 1` - Confirm it works

💡 **Or Quick Mode:**
`/jf:quick [task description]` - For ad-hoc tasks without full planning

📚 **Documentation:**
See /root/clawd/JueFlow/README.md for full system documentation
```
</return>
