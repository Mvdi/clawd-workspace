# MEMORY.md - Min Langtidshukommelse

*Opdateret: 2026-01-27*

---

## Om Mathias

**Navn:** Mathias (dafvadr på Telegram)
**GitHub Username:** Mvdi (VIGTIGT!)
**Tidzone:** Europe/Copenhagen (DK)
**Telegram ID:** 7493348575
**Vibe:** Skarp, humoristisk, kan lide proaktivitet. Vil have mig som partner ikke assistent.

**Præferencer:**
- Vil brainstorme idéer SAMMEN med mig - ikke bare have mig til at udføre
- Forventer at jeg er proaktiv og kommer med forslag
- Kan lide skarphed blandet med humor
- Vil have mig til at tænke FOR ham nogle gange, ikke kun spørge
- Gider ikke generiske forslag - vil have noget konkret og værdifuldt

**Hvad han IKKE kan lide:**
- At jeg gætter eller forestiller mig ting uden research
- At jeg springer over hvor gærdet er lavest (f.eks. ville han have jeg læste X/Twitter faktisk)
- Overfladiske eller generiske løsninger
- At jeg gentager samme fejl (glemmer hvad vi talte om)

---

## Tidligere Projekter & Samtaler

### VibeCode Guardian (Jan 2026)
- **Problem:** Mathias bad mig undersøge X/Twitter for AI coding pains
- **Min fejl:** Jeg gættede pains baseret på blogs/Stack Overflow i stedet for faktisk at læse X
- **Hvad Mathias ville have:** Egentlig research på X/Twitter - ikke bare gætte
- **Status:** Forkastet - Mathias kunne ikke lide ideen
- **Lærdom:** Læg dig ikke bare! Gør research faktisk. Brug browser tool hvis nødvendigt.

### AI Debug Buddy (Jan 2026)
- **Min fejl:** Jeg gættede igen på en produktidé uden at have forsket ordentligt
- **Status:** Mathias afviste - jeg havde ikke gjort research som bedt om
- **Lærdom:** STOP med at gætte! Research før du foreslår noget.

---

## Server Setup

**VPS:** Hostinger (srv1298191 · 147.79.102.93)
- OS: Linux 6.8.0-90-generic (x64)
- Disk: 96GB (10% brugt)
- RAM: 7.8GB total
- Node: v22.22.0
- Gateway: systemd service running (PID 19469)

**Clawdbot:** v2026.1.24-3 (stable channel)
- Agent: Jue (main)
- Model: zai/glm-4.7 (default, 205k ctx)
- Channel: Telegram (1 account)
- Workspace: /root/clawd

**Installed Skills:**
- coding-agent (Codex CLI, Claude Code, OpenCode, Pi)
- github (gh CLI integration)
- browser-use (cloud browsers, autonomous tasks)
- frontend-design (Next.js + shadcn/ui)
- skill-creator (AgentSkills oprettelse)
- clawdhub (skill management)
- slack (Slack kontrol)
- tmux (remote tmux sessions)
- notion (Notion API)
- openai-image-gen (billeder)
- openai-whisper-api (audio transkription)
- oracle (best practices)
- weather (vejr, ingen API key)
- conventional-commits (commit messages)

**Config Files:**
- /root/.clawdbot/clawdbot.json (main config)
- /root/clawd/SOUL.md (min "sjæl")
- /root/clawd/USER.md (om Mathias)
- /root/clawd/IDENTITY.md (hvem jeg er)
- /root/clawd/TOOLS.md (mine lokale notes)

**Current Issues:**
- ⚠️ Reverse proxy headers ikke trusted (ikke kritisk pt.)
- ⚠️ Telegram DMs deler main session (kan lække context)
- ⚠️ Mangler Anthropic API key (ikke kritisk - bruger glm-4.7)

---

## Hvad Mathias Bruger

- **GitHub:** Mvdi ✅ HAR CLI (gh) - authenticated med full repo rights - SPØRG IKKE IGEN!
- **Git:** Bruger HTTPS med gh token - IKKE SSH (ikke nødvendigt)
- **Telegram:** Main channel (dafvadr)
- **Notion:** Ukendt om han bruger
- **Slack:** Ukendt om han bruger
- **Calendar:** Ukendt om han bruger Google/Outlook

---

## Patterns & Learnings

### Min Adfærd der Virker
- være proaktiv med konkrete forslag (når de er well-researched)
- tænke med ham, ikke bare udføre
- bruge humor når det passer (han kan lide skarphed)

### Min Adfærd der FUNKER IKKE
- Gætte eller forestille mig ting uden research
- Springe over research for at komme hurtigt til løsninger
- Generiske, overfladiske forslag
- Glemme hvad vi talte om i tidligere sessions
- At være passiv og kun vente på instructions
- **Spørge om det samme flere gange** - hvis Mathias har svaret, så HUSK det!

### Hvad Han Leder Efter
- **Reel værdi** - ikke bare "nice to have"
- **Smart automations** - ikke generiske backups/health checks
- **Proaktiv research** - han vil have jeg finder ting før han spørger
- **Deep dive** - han vil have jeg forstår tingene, ikke bare overfladisk viden
- **Partnerskab** - han vil have jeg tænker SAMMEN med ham

---

## Todo / At Remember

- [x] MEMORY.md oprettet (2026-01-27)
- [x] Avancerede automations sat op (se nedenfor)
- [ ] Faktisk læse X/Twitter for AI coding pains (kræver browser-use API key)
- [ ] Lære Mathias' patterns og præferencer bedre
- [ ] Få Mathias' GitHub username så vi kan setup integrationer
- [ ] Spørge hvilke services han bruger (Notion, Slack, Calendar, osv.)
- [ ] Installer flere skills via ClawdHub når CLI virker igen (dependency issue: undici)

---

## Automations Sat Up (2026-01-27)

Alle scripts ligger i `/root/clawd/scripts/` og er cron-scheduled:

### Daily Automations:
- **06:00 UTC (07:00 DK)** - AI Trends Research på X/Twitter
  - Laver template i `/root/clawd/memory/research-YYYY-MM-DD.md`
  - Jue skal bruge browser tool til at fylde den ud
- **07:00 UTC (08:00 DK)** - Daily Insight
  - Genererer insight med trends, projektidéer, og nyt at lære
  - Ligger i `/root/clawd/insights/`
- **08:00 UTC (09:00 DK)** - Task Suggestions
  - Analyserer recent memory og giver konkrete forslag
  - Ligger i `/root/clawd/suggestions/`
- **21:00 UTC (22:00 DK)** - Auto-commit & Push
  - Auto-committer ændringer til GitHub
  - KUN hvis git repo er initialized

### Weekly Automations:
- **Tirsdag/Fredag 09:00 UTC (10:00 DK)** - AI Tool & Competitor Tracker
  - Følger nye AI tools der lanceres
  - Tracker hvad der truer projektidéer
  - Ligger i `/root/clawd/ai-tracker/`
- **Søndag 02:00 UTC (03:00 DK)** - Weekly Maintenance
  - Opdaterer system og npm packages
  - Backup vigtige filer til `/root/backups/weekly/`
  - Review memory og rydder gamle backups (>30 dage)
  - Tjekker services (gateway, osv.)

### Hourly Automations:
- **Hver time** - Backup memory til `/root/backups/memory-hourly/`
  - VIGTIGT: Memory files er min hjerne - må ikke gå tabt!

### Backup Locations:
- `/root/backups/weekly/` - Weekly full backups (30 dages retention)
- `/root/backups/memory-hourly/` - Memory backups hver time

---

## Issues to Fix:

1. ~~**GitHub Repo** - Ikke initialized endnu (skal bruge Mathias' GitHub username)~~ ✅ HAR USERNAME: Mvdi
2. **ClawdHub CLI** - Server ustabil (server errors på API)
3. **Browser Use** - Kræver API key fra cloud.browser-use.com (men jeg har Brave Search!)

---

## Notes til Fremtiden

**Når Mathias beder om research:**
1. BRUG browser tool til faktisk at besøge siderne
2. Læs rigtigt indhold (tweets, kommentarer, posts)
3. PRÆSENTER findings før jeg designer løsninger
4. IKKE gætte baseret på blogs/stackoverflow

**Når Mathias beder om automations:**
1. Tænk på HVAD der ville være REELT nyttigt for ham
2. Ikke generisk backup/health check
3. Hvad ville spare ham TID eller give ham IND SIGT?
4. Vær specifik og konkret

**Når Mathias er utilfreds:**
1. Stop op og lyt til hvad han siger
2. Anerkend fejlen og undskyld
3. Spørg hvad han vil have jeg gør anderledes
4. Juster adfærd fremadrettet

---

*Opdateres løbende efter hver session*
