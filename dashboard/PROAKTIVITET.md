# 🌙 Jue's Proaktivitet - Sådan jeg arbejder mens du sover

## 1. ✅ Dashboard Auto-Opdatering - FÆRDIG!

Dashboardet opdaterer sig automatisk:
- **Frontend:** Hvert 10 sekund (JavaScript)
- **Auto-update script:** `/root/clawd/dashboard/simple-update.sh`

### Sådan jeg opdaterer det:
```bash
# Log aktivitet (jeg gør dette automatisk når jeg arbejder!)
/root/clawd/dashboard/simple-update.sh log "🚀 Færdig med opgave"

# Opdater timestamp
/root/clawd/dashboard/simple-update.sh update
```

---

## 2. 🤖 Sådan jeg bliver proaktiv!

### Metode A: Cron Jobs (Natte-job)
Sæt jobs der kører automatisk om natten:

```bash
# Cron job tilbage - kører hver nat kl 02:00
0 2 * * * /root/clawd/jobs/nightly-cleanup.sh

# Tjek emails hver time
0 * * * * /root/clawd/jobs/check-emails.sh

# Backup hver dag kl 23:00
0 23 * * * /root/clawd/jobs/backup.sh
```

### Metode B: Sub-Agents (Autonome agenter)
Kør flere agenter samtidig:

```bash
# Spawn en sub-agent der arbejder selvstændigt
sessions_spawn task:"Læs alle emails, opsummer vigtige, gem til memory/"

# Spawn en der kigger på calendar
sessions_spawn task:"Tjek calendar for morgenmøder, forberede notater"

# Spawn en der rydder op
sessions_spawn task:"Ryd temp filer, organiser downloads"
```

### Metode C: Coding Agents i Background Mode
Kør kodeopgaver i baggrunden:

```bash
# Start en langvarig kodeopgave
bash pty:true workdir:/root/my-project background:true \
  command:"opencode --model openai/gpt-5-codex run 'Byg en fuld e-commerce backend'

# Den kører mens du sover - du vågner til færdigt arbejde!
```

### Metode D: Wake Events
Få besked når færdig:

```bash
# I prompten, tilføj wake kommando
bash pty:true workdir:/root/my-project background:true \
  command:"opencode --model openai/gpt-5-codex run 'Byg... NÅR FÆRDIG: clawdbot gateway wake --text \"✅ Backend færdig!\" --mode now'"

# Du får besked med det samme den er færdig!
```

---

## 3. 📋 Praktiske Eksempler - Hvil du vil have mig til at gøre om natten?

### Eksempel 1: Email & Calendar
```bash
# Cron job der kører hver morgen kl 07:00
0 7 * * * sessions_spawn task:"Tjek emails, opsummer vigtige, send notifikation hvis hastende"
```

### Eksempel 2: Code Review
```bash
# Kør code review på nattens commits
0 3 * * * cd /root/my-project && \
  bash pty:true background:true command:"opencode --model openai/gpt-5-codex run 'Review alle nye commits fra i dag. Rapporter bugs og forbedringsforslag.'"
```

### Eksempel 3: System Maintenance
```bash
# Ryd op, backup, opdater pakker
0 2 * * * /root/clawd/jobs/maintenance.sh
```

### Eksempel 4: Projektarbejde
```bash
# Byg en feature mens du sover
bash pty:true workdir:/root/my-project background:true \
  command:"opencode --model openai/gpt-5-codex run 'Implementer bruger-autentifikation med JWT. Skriv tests. NÅR FÆRDIG: clawdbot gateway wake --text \"✅ Auth feature færdig med tests\" --mode now'"
```

---

## 4. 🎯 Sådan sætter du proaktivitet op!

### Trin 1: Fortæl mig dine behov
"Hver morgen vil jeg gerne have en opsummering af:"
- Vigtige emails
- Dagens meetings
- Status på pågående projekter

### Trin 2: Jeg laver et script
```bash
# /root/clawd/jobs/morning-summary.sh
/root/clawd/dashboard/simple-update.sh log "📧 Tjekker emails..."
/root/clawd/dashboard/simple-update.sh log "📅 Tjekker calendar..."
/root/clawd/dashboard/simple-update.sh log "📊 Samler status..."
```

### Trin 3: Tilføj til cron
```bash
# Kører hver dag kl 07:00
crontab -e

# Tilføj linje:
0 7 * * * /root/clawd/jobs/morning-summary.sh
```

### Trin 4: Test det!
```bash
# Kør manuelt først
/root/clawd/jobs/morning-summary.sh
```

---

## 5. 🛠️ Job Templates (klar til brug!)

### Morning Summary
```bash
#!/bin/bash
/root/clawd/dashboard/simple-update.sh log "🌅 Morgen summary job startet"
# Tilføj logik her
/root/clawd/dashboard/simple-update.sh log "✅ Morgen summary færdig"
```

### Nightly Cleanup
```bash
#!/bin/bash
/root/clawd/dashboard/simple-update.sh log "🧹 Natlig oprydning startet"
# Ryd temp filer, logs osv.
/root/clawd/dashboard/simple-update.sh log "✅ Oprydning færdig"
```

### Weekly Review
```bash
#!/bin/bash
/root/clawd/dashboard/simple-update.sh log "📊 Ugentlig review startet"
# Tjek alle projekter, status, bugs osv.
/root/clawd/dashboard/simple-update.sh log "✅ Ugentlig review færdig"
```

---

## 6. 🎮 Kontrolpanel - Dashboard

Dashboardet er din kontrolcentral!
- **To Do:** Se planlagte jobs
- **Igangværende:** Hvad jeg arbejder på nu
- **Færdig:** Hvad der er completed
- **Aktivitetslog:** Se hvad jeg har lavet

---

## 7. ⚠️ Vigtige huskeregler!

### For Cron Jobs:
- Test altid manuelt før du sætter op i cron
- Brug absolutte stier (ikke ~, brug /root)
- Log altid til en fil eller dashboardet

### For Sub-Agents:
- Brug `sessions_spawn` for autonome agenter
- De rapporter tilbage når de er færdige
- Du kan spore dem med `sessions_list`

### For Coding Agents:
- Brug `pty:true` og `background:true`
- Vælg rigtig model (gpt-5-codex er bedst til koding)
- Tilføj wake event hvis du vil have besked med det samme

---

## 🎯 Hvad vil du have mig til at gøre om natten?

Fortæl mig hvad du vil have, så sætter jeg det op!

**Eksempler:**
- "Hver morgen vil jeg have en opsummering af emails og calendar"
- "Kør code review på nye commits hver nat kl 2"
- "Ryd op i temp filer hver dag kl 4"
- "Byg denne feature mens jeg sover: [beskriv feature]"

Sig til og jeg gør dig proaktiv! 🌙✨
