---
name: jueflow
description: Automated reliable workflows for project building - multi-agent orchestration, fresh context windows, atomic commits. Use when starting new projects, planning complex features, or running autonomous overnight builds.
metadata: {"clawdbot":{"requires":{"bins":["git"]},"install":[{"id":"shell","kind":"copy","label":"Copy skill files to workspace"}]}}
---

# JueFlow - Automated Reliable Workflows

**Inspired by:** [Get Shit Done](https://github.com/glittercowboy/get-shit-done)

**Core Problem Solved:** Context rot → AI quality degrades as context window fills, leading to inconsistent, buggy code.

**JueFlow Solution:**
- Fresh context windows per task (200k tokens pure implementation)
- Multi-agent orchestration (parallel researchers, atomic executors)
- State tracking (PROJECT.md, STATE.md, REQUIREMENTS.md, ROADMAP.md)
- Atomic git commits (surgical, traceable, meaningful)
- Verification before completion (goals checked against codebase, not assumed)

---

## When to Use This Skill

Use JueFlow when:
- **Starting a new project** - Full workflow: research → plan → build → verify
- **Building complex features** - Multi-phase breakdown, parallel execution
- **Overnight autonomous builds** - Define before sleep, wake up to verified work
- **Need reliable quality** - Fresh context prevents degradation
- **Want atomic commits** - Clean git history, easy debugging

**Don't use for:**
- Simple ad-hoc commands (just write code directly)
- Quick questions without follow-through
- Non-project tasks (research, brainstorming without building)

---

## Quick Start

### Initialize New Project
```
"Start a JueFlow project to build [your idea]"
```
Or more specific:
```
"Use JueFlow to create a new project for building X"
```

This triggers the full workflow:
1. Questions → Understand project fully
2. Project Researcher → Survey domain ecosystem
3. Requirements extraction → v1 vs v2 vs out of scope
4. Roadmap creation → Phases mapped to requirements
5. Approval → Ready to build

### Execute Phase Autonomously
```
"Use JueFlow to execute phase 1" or "Run JueFlow for phase 1 execution"
```
- Spawns parallel executors with fresh 200k context each
- Runs all night, atomic commits per task
- Wake up to verified work with clean git history

### Quick Ad-hoc Task
```
"Use JueFlow for a quick task: fix login bug"
```
- Atomic plan + implementation + commit (no research overhead)

---

## File Structure

All JueFlow files live in `.planning/`:

```
.planning/
├── PROJECT.md           # Project vision, always loaded
├── STATE.md            # Decisions, blockers, position
├── REQUIREMENTS.md     # Scoped v1/v2 requirements
├── ROADMAP.md          # Phases, milestones, progress
├── research/           # Ecosystem research
│   ├── SUMMARY.md
│   ├── STACK.md
│   ├── FEATURES.md
│   ├── ARCHITECTURE.md
│   └── PITFALLS.md
└── phases/             # Phase-specific files
    ├── phase1-CONTEXT.md       # Your decisions
    ├── phase1-RESEARCH.md      # Research findings
    ├── phase1-1-PLAN.md        # Atomic tasks
    ├── phase1-1-SUMMARY.md    # What happened
    └── phase1-VERIFICATION.md # Goals vs reality
```

---

## Workflow Commands

### Core Workflow
1. **New Project** - "Use JueFlow to start a new project for [description]"
   → Creates: PROJECT.md, REQUIREMENTS.md, ROADMAP.md, STATE.md, research/

2. **Discuss Phase** - "Use JueFlow to discuss phase 1 implementation"
   → Creates: {phase}-CONTEXT.md (your decisions before planning)

3. **Plan Phase** - "Use JueFlow to plan phase 1"
   → Creates: {phase}-RESEARCH.md, {phase}-{N}-PLAN.md (atomic task plans)

4. **Execute Phase** - "Use JueFlow to execute phase 1"
   → Creates: {phase}-{N}-SUMMARY.md + git commits (autonomous overnight builds!)

5. **Verify Work** - "Use JueFlow to verify phase 1"
   → Creates: {phase}-UAT.md + fix plans if issues found

6. **Complete Milestone** - "Use JueFlow to complete the current milestone"
   → Archives milestone, tags release, ready for next

### Quick Tasks
- **Quick Mode** - "Use JueFlow for a quick task: [description]"
   → Atomic plan + implementation + commit (no research, no verification overhead)

### Navigation
- **Progress** - "Show JueFlow progress" or "What's the status of JueFlow?"
   → Current phase, tasks completed, what's next

- **Help** - "Show JueFlow commands" or "JueFlow help"
   → Full command reference

---

## Agent System

JueFlow uses specialized agents, each with a specific role:

| Agent | Role | Triggered By |
|--------|------|--------------|
| **Project Researcher** | Surveys domain ecosystem, finds tech stack, maps features, catalogs pitfalls | New project / New milestone |
| **Phase Researcher** | Deep dive into specific phase implementation options | Plan phase |
| **Planner** | Creates atomic task plans with XML structure | Plan phase |
| **Executor** | Implements tasks, each with fresh 200k context | Execute phase |
| **Verifier** | Confirms code delivers what was promised | Verify work |
| **Debugger** | Diagnoses failures systematically | Auto-triggered on verification fail |

**Orchestrator Pattern:**
Each stage spawns parallel agents, waits for completion, integrates results, routes to next stage.
**Result:** Main context stays at 30-40%. Work happens in fresh subagent contexts.

---

## XML Task Format

Every plan uses XML optimized for LLMs:

```xml
<task type="auto|manual">
  <name>Create login endpoint</name>
  <files>src/app/api/auth/login/route.ts</files>

  <dependencies>
    <dep task="2">Requires users table from task 1</dep>
  </dependencies>

  <action>
    Use jose for JWT (not jsonwebtoken - CommonJS issues).
    Validate credentials against users table.
    Return httpOnly cookie on success.
  </action>

  <verify>
    curl -X POST localhost:3000/api/auth/login returns 200 + Set-Cookie
  </verify>

  <done>
    Valid credentials return cookie, invalid return 401
  </done>
</task>
```

**Why XML?** Precise instructions. No guessing. Verification built in. Easy parsing by executors.

---

## Key Principles

1. **Fresh Context Every Task** - No accumulation, no degradation
2. **Multi-Agent Parallelism** - Independent tasks run simultaneously
3. **Atomic Verification** - Each task verified before commit
4. **Clean Git History** - Bisect works, rollback is surgical
5. **Walk Away, Come Back Done** - Full autonomy with verification

---

## Overnight Execution

**Scenario:** Mathias sleeps 8 hours, Jue builds entire milestone

```
Before sleep:
1. "Use JueFlow to start a new project for X"
2. "Use JueFlow to discuss phase 1"
3. "Use JueFlow to plan phase 1"

Sleep 8 hours → Jue runs autonomously:
4. "Use JueFlow to execute phase 1" (all night, parallel executors)

Wake up → Verified work, clean git history, ready to ship:
5. "Use JueFlow to verify phase 1" (morning check - does it work?)
```

---

## Configuration

`.planning/config.json` controls behavior:

```json
{
  "mode": "interactive",
  "depth": "standard",
  "profiles": {
    "planning": "quality|balanced|budget",
    "execution": "balanced",
    "verification": "standard"
  },
  "workflows": {
    "research": true,
    "plan_check": true,
    "verifier": true
  },
  "execution": {
    "parallel": true,
    "commit_docs": true
  }
}
```

- **mode:** `interactive` (confirm each step) or `yolo` (auto-approve)
- **depth:** `quick` (fast), `standard` (balanced), `comprehensive` (deep)
- **profiles:** Balance quality vs token cost

---

## Files & Location

**Skill files in workspace:** `skills/jueflow/`
- SKILL.md (this file)
- _meta.json
- agents/ (project-researcher, planner, executor, verifier, debugger)
- commands/ (command templates)
- scripts/ (shell scripts)

**Project files created during use:** `.planning/` (in current working directory)

---

## Example Session

```
User: "Use JueFlow to start a new project for building a simple todo app"

JueFlow:
1. [Questions] What tech stack? What features? What's MVP scope?
2. [Project Researcher] Surveys todo app ecosystem, recommends React + Node + SQLite
3. [Requirements] Extracts v1 (add, list, delete tasks)
4. [Roadmap] Creates 3 phases: setup, core features, polish

User: "Use JueFlow to discuss phase 1"

JueFlow:
- [Questions] Do you want dark mode? How should tasks be ordered?

User: "Use JueFlow to plan phase 1"

JueFlow:
- [Phase Researcher] Investigates setup patterns
- [Planner] Creates 3 atomic task plans with XML

User (before sleep): "Use JueFlow to execute phase 1"

JueFlow (overnight):
- [Executor 1] Sets up Next.js project + commits
- [Executor 2] Sets up SQLite database + commits
- [Executor 3] Creates base UI components + commits

User (morning): "Use JueFlow to verify phase 1"

JueFlow:
- [Verifier] Walks through: Can you add a task? Can you list tasks?
- [Result] ✅ All verified or → creates fix plans

User: "Use JueFlow to complete the milestone"

JueFlow:
- Tags v1.0 release, archives docs, ready for v2
```

---

## Why This Works

1. **Complexity in system, simplicity in interface** - You see simple commands, system handles multi-agent orchestration
2. **Fresh context per task** - 200k tokens pure implementation, zero accumulated garbage
3. **Parallel execution** - Independent tasks run simultaneously
4. **Verification before trust** - Goals checked against codebase
5. **Atomic commits** - Each task independently revertable, clean history

---

*Built by Jue for automated reliable workflows 🧙‍♂️*
