# JueFlow Test & Demo - Todo App

## Projekt: JueFlow Todo Manager

**Mål:** Vise hvordan JueFlow virker ved at bygge en simpel todo app med det.

**Tech Stack:**
- Frontend: Next.js 14 (App Router) + shadcn/ui (komponenter)
- Backend: Next.js API routes
- Styling: Tailwind CSS
- Database: In-memory (todos array - kan udvides senere)

---

## Features

### Core Functionality
- ✅ Tilføj nye todos
- ✅ List alle todos (Alle/Åbne/Færdige)
- ✅ Marker todo som færdig (toggle)
- ✅ Slet todos
- ✅ Filter efter status (Alle/Åbne/Færdige)
- ✅ Filter efter prioritet (Høj/Medium/Lav)
- ✅ Sortering (Nyeste først)

### JueFlow Integration
- Viser hvordan JueFlow agents ville arbejde på dette projekt:
  - **Project Researcher:** Analyserer "todo management" domain
  - **Planner:** Laver task plans: "create todo API endpoint", "build frontend UI"
  - **Executor:** Implementerer tasks med fresh context
  - **Verifier:** Bekræfter at todos virker som forventet

---

## Implementation Plan

### Phase 1: Backend API (Next.js)
```
/api/todos
  GET     - Hent alle todos
  POST    - Opret ny todo
  PUT     - Opdater todo (id, status, text, priority)
  DELETE  - Slet todo
  PATCH   - Toggle status (todo ↔ done)
  ?filter - Filtrer (status, priority)
```

### Phase 2: Frontend UI (Next.js + shadcn/ui)
```
/app/todos (Simple todo list)
  - Card for hver todo med:
    - Titel
    - Beskrivelse
    - Prioritet (Høj/Medium/Lav) - badge
    - Status (Åben/Færdig) - checkbox
    - Knap: Slet
    - Knap: Mark færdig
  - Filter knapper: Alle/Åbne/Færdige/Høj/Medium/Lav

/components/ui/ (Reusable komponenter)
  - Button
  - Card
  - Badge
  - Checkbox
```

---

## JueFlow Agent Roles for Dette Projekt

### Project Researcher
- Undersøger "todo management" domain
- Finder best practices (Next.js, state management, CRUD APIs)
- Identificerer patterns (id generation, timestamp tracking)

### Planner
- Laver task plans:
  1. "Setup Next.js project structure"
  2. "Create /api/todos CRUD routes"
  3. "Implement todo model (id, title, description, priority, status, created, updated)"
  4. "Setup shadcn/ui with Next.js"
  5. "Create /app/todos page with filtering"
  6. "Add JueFlow integration documentation"

### Executor
- Kører hver plan med fresh 200k context:
  - `npx create-next-app@latest` (init projekt)
  - Koder API routes (`src/app/api/todos/route.ts`)
  - Koder todo model (`src/models/todo.ts`)
  - Laver shadcn komponenter (`components/ui/*.tsx`)

### Verifier
- Bekræfter:
  - API virker (test med curl)
  - Frontend loader todos
  - Sætte todo virker (API kald)
  - Slet todo virker (API kald)

---

## Tidsestimering

| Fase | Estimeret tid | Hvem gør det |
|------|--------------|----------------|
| 1. Project setup | 15 min | Mathias (setup) |
| 2. Backend API | 30 min | Jue (executor) |
| 3. Frontend UI | 45 min | Mathias (executor) |
| 4. Integration & test | 15 min | Mathias + Jue |
| **TOTAL** | **~1.5 time** | |

---

## Hvad Du Får

### 1. Et Færdigt Produkt
- Full-stack todo app med JueFlow demonstration
- Viser hvordan multi-agent system fungerer i praksis
- Kan bruges som reference for fremtidige JueFlow projekter

### 2. Viden Om JueFlow
- Du ser exakt hvordan hver agent (researcher, planner, executor) arbejder
- Forstår XML task format og hvorfor det er effektivt
- Ser hvordan friske context windows forhindrer degradation

### 3. Test Ground for Andre Projekter
- Hvis du senere vil have et projekt (f.eks. "analyser X/Twitter for AI pains"), så kan du se:
  - "Kør /jf:new-project 'analyser X/Twitter'"
  - JueFlow vil automatisk:
    - Spørge om projektet
    - Undersøge "X/Twitter analysis" domain
    - Lave requirements og roadmap
    - Plan og execute faser
  - Du får forskning på hvordan det virker!

---

## Næste Skridt Efter Demo

### Option A: Forklæg til Rigting Projekt
Hvis du har et rigtigt projekt, så:
- JueFlow tager over og gør alt arbejde
- Researcher, planlægger, eksekverer automatisk
- Du godkender bare og reviewer koden

### Option B: Videreudvikling af Todo App
Vi kan:
- Tilføj real database (PostgreSQL, SQLite, Supabase)
- Implementere user authentication
- Tilføj collaboration features (delt lister)
- Lave mobil app (React Native)

### Option C: Andet
Hvis du vil have jeg gør noget helt andet, så fortæl mig!

---

## Start Projekt Nu?

**Kør:** `/jf:quick "Byg en todo app med JueFlow integration"`

**Eller:** Svar "A", "B", eller "C" for at jeg starter den rette handling! 🚀

---

*JueFlow integration demo projekt*