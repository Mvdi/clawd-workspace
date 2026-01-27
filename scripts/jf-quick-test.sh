#!/bin/bash
# JueFlow Quick - Start simpel todo projekt
# Dette script insterer JueFlow systemet

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}🧙‍♂️ JueFlow - Quick Task${NC}"
echo ""
echo "Insterer JueFlow systemet..."
echo ""

# Kopier JueFlow filer til workspace
JUEFLOW_DIR="/root/clawd/JueFlow"

if [ ! -d "/root/clawd/JueFlow" ]; then
    mkdir -p "/root/clawd/.planning/research" "/root/clawd/.planning/phases"
    
    echo -e "  ✅ Directory structure oprettet${NC}"
    echo "     /root/clawd/.planning/"
    echo "         ├── research/"
    echo "         └── phases/"
else
    echo -e "  ⚠️  .planning findes allerede${NC}"
    echo "     Kører videre..."
fi

# Sæt op projekt
PROJECT_DESC="En simpel todo app til at vise JueFlow systemet"
echo "Projekt: $PROJECT_DESC" > /tmp/jueflow-input.txt

# Simuler Project Researcher Agent
echo ""
echo -e "${YELLOW}📡 1. Project Researcher Agent${NC}"
echo "Analysering: $PROJECT_DESC"
echo ""

# Skab initiale filer
cat << 'EOF' > /root/clawd/.planning/PROJECT.md
# Todo App - JueFlow Demo

## Vision
Vis hvordan JueFlow multi-agent system fungerer ved at bygge en simpel todo app.

## Goals
- Demonstrer Project Researcher → Planner → Executor → Verifier workflow
- Vise atomic commits per task
- Vise fresh 200k context windows
- Vise state tracking (PROJECT.md, STATE.md, REQUIREMENTS.md, ROADMAP.md)

## Success Criteria
- Frontend: Next.js + shadcn/ui komponenter viser todos
- Backend: Next.js API med CRUD operations (/api/todos)
- JueFlow integration: Hver todo er en "phase" i JueFlow systemet
- Atomic commits: Hver opdatering får eget commit
- Clean git history: Git bisect virker, rollback er simpel

## Constraints
- Brug JueFlow templates til phases og tasks
- Brug XML task format (som GSD)
- Frisk 200k context per executor task
- Verification før completion

## Tech Stack
- Frontend: Next.js 14, shadcn/ui, Tailwind CSS
- Backend: Next.js 14 (App Router), in-memory database (todos array)
- Git: gh CLI for auto-commit og push

## Timeline
- MVP: ~2-3 timer
- Full demo: ~4-6 timer
EOF

echo -e "  ✅ PROJECT.md oprettet${NC}"

# Skab STATE.md
cat << 'EOF' > /root/clawd/.planning/STATE.md
# Todo App - JueFlow Demo - State

## Current Phase
Not Started

## Phase Status

| Phase | Name | Status | Started | Completed |
|-------|------|--------|----------|
| 1 | Initialization | Done | $(date +%Y-%m-%d) |

## Decisions Log
- [Date] - Beslutning - Årsag: [Hvorfor]

## Blockers
None currently

## Notes
Dette projekt vil demonstrere JueFlow systemet med en simpel todo app.
EOF

echo -e "  ✅ STATE.md oprettet${NC}"

# Skab REQUIREMENTS.md
cat << 'EOF' > /root/clawd/.planning/REQUIREMENTS.md
# Todo App - JueFlow Demo - Requirements

## v1 (MVP) Must-Haves

### Core Functionality
- Frontend: Next.js 14 app der viser todos
- Backend: Next.js API med CRUD operations
  - GET /api/todos - Hent alle todos
  - POST /api/todos - Opret ny todo
  - PUT /api/todos/:id - Opdater todo
  - DELETE /api/todos/:id - Slet todo
  - PATCH /api/todos/:id/toggle - Toggle status (todo ↔ done)
- Filtering: Status filter (All/Active/Completed), Prioritet filter (Høj/Medium/Lav)

### JueFlow Integration
- Hver todo bliver behandlet som en "phase" i JueFlow systemet
- Project Researcher Agent analyserer "todo management" domain
- Planner Agent laver task plans (XML format)
- Executor Agent implementerer tasks med frisk 200k context
- Verifier Agent bekræfter goals før completion

### Data Model
- In-memory todos array i backend (ingen database i MVP)
- Frontend henter todos fra API

### Git Integration
- Auto-commit hver aften kl 22:00 DK via cron
- Push til GitHub: https://github.com/Mvdi/clawd-workspace.git
- Konvententionel commit messages: "feat(todo): [beskrivelse]"

## v1 Nice-to-Haves

- Dark mode toggle
- Prioritet farver badges (Rød/Hvid/Grøn)
- Sorterings (Nyeste først, Ældste først)
- Søge felt
- Todo detaljer (modal popup)

## Out of Scope (v2+)

- Database (PostgreSQL, SQLite, Supabase)
- User authentication (Login, register, JWT)
- Real-time collaboration (WebSockets)
- Advanced filtre og views

## Non-Functional

- Mobile app
- Email notifikationer
- Cloud sync
EOF

echo -e "  ✅ REQUIREMENTS.md oprettet${NC}"

# Skab ROADMAP.md
cat << 'EOF' > /root/clawd/.planning/ROADMAP.md
# Todo App - JueFlow Demo - Roadmap

## Milestone: v1 - JueFlow Demo

### Phase 1: Initialization ✅ (DONE)
- [x] PROJECT.md - Projekt vison og success criteria
- [x] STATE.md - Current phase og blockere log
- [x] REQUIREMENTS.md - v1 must-haves og nice-to-haves
- [x] Roadmap - Faser planlægges til v1

### Phase 2: Backend API ⏳ (IN PROGRESS)
- [ ] Opsæt Next.js project structure
- [ ] Implementer todos data model (in-memory array)
- [ ] Implementer CRUD endpoints:
  - [ ] GET /api/todos - Hent alle todos
  - [ ] POST /api/todos - Opret ny todo
  - [ ] PUT /api/todos/:id - Opdater todo
  - [ ] DELETE /api/todos/:id - Slet todo
  - [ ] PATCH /api/todos/:id/toggle - Toggle status
- [ ] Filtrering endpoints:
    - [ ] GET /api/todos?status= (All/Active/Completed)
    - [ ] GET /api/todos?priority= (Høj/Medium/Lav)
- [ ] GET /api/todos?assignee= (Filter by assignee)

### Phase 3: Frontend UI ⏳ (PLANNED)
- [ ] Opsæt Next.js 14 med App Router
- [ ] Installerer shadcn/ui komponenter
- [ ] Implementer TodoPage (liste, filtre, sortering)
- [ ] Implementer CreateTodo modal (titel, beskrivelse, prioritet)
- [ ] Implementer Filter komponenter (status knapper, prioritet dropdown)
- [ ] Implementer TodoCard komponent (visning, status checkbox, slet knap)
- [ ] Implementer Sorter komponenter (Nyeste først, Ældste først)
- [ ] Styling med Tailwind CSS

### Phase 4: JueFlow Integration ⏳ (PLANNED)
- [ ] Simuler Project Researcher Agent
- [ ] Simuler Planner Agent (laver task plans)
- [ ] Simuler Executor Agent (implementerer tasks)
- [ ] Simuler Verifier Agent (tjekker goals)
- [ ] Test XML task format
- [ ] Test atomic commits

### Phase 5: Git Integration ⏳ (PLANNED)
- [ ] Opsæt GitHub CLI (gh) med repo authentication
- [ ] Implementer auto-commit script
- [ ] Implementer auto-push til Mvdi/clawd-workspace.git
- [ ] Test konventionel commit messages
- [ ] Opsæt cron job (22:00 DK)

### Phase 6: Testing & Demo ⏳ (PLANNED)
- [ ] Test frontend UI (rendering, interaktioner)
- [ ] Test backend API (alle CRUD operations)
- [ ] Test JueFlow integration (fases som "phases")
- [ ] Test Git auto-commit og push
- [ ] Bug fixes og optimering
- [ ] End-to-end test af fuldt workflow
- [ ] Demo for Mathias (live demo eller video walkthrough)

---

## Milestone: v2 (FUTURE)
- Database (PostgreSQL eller SQLite)
- User authentication (Login, register, JWT)
- Real-time collaboration
- Advanced filtre og views
- Mobile app

---

## Project Details

- **GitHub:** https://github.com/Mvdi/jueflow-demo-todo
- **Tech Stack:** Next.js 14 + shadcn/ui + JueFlow agents
- **Estimated Time:** 4-6 timer til MVP
EOF

echo -e "  ✅ ROADMAP.md oprettet${NC}"

echo ""
echo -e "${GREEN}📋 Projekt oprettet!${NC}"
echo -e "   Name: Todo App - JueFlow Demo"
echo -e "   Vision: Vise JueFlow multi-agent system i praksis"
echo -e "   Tech: Next.js + JueFlow agents"
echo ""
echo -e "${GREEN}🗺  Faser planlagt i ROADMAP.md${NC}"
echo -e "   Phase 2: Backend API (IN PROGRESS) - næste skridt"
echo -e "   Phase 3-6: Frontend, JueFlow integration, Git, Testing"
echo ""
echo -e "${YELLOW}⏳  Næste: Implementer Backend API${NC}"
echo "   Opsæt Next.js project structure"
echo -   Implementer todos data model"
echo "   Implementer CRUD endpoints"
echo ""
echo -e "${GREEN}✅ JueFlow systemet er nu klar til brug!${NC}"
echo ""
echo -e "Project filer:"
echo -e "  /root/clawd/.planning/PROJECT.md"
echo -e "  /root/clawd/.planning/STATE.md"
echo -e "  /root/clawd/.planning/REQUIREMENTS.md"
echo -e "  /root/clawd/.planning/ROADMAP.md"
