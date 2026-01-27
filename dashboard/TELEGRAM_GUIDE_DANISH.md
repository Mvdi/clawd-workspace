# 📱 Telegram Integration Setup Guide

## 🎯 Hvad jeg kan gøre vs hvad der kræves

### ✅ Hvad JUE kan gøre (nu):
- Opdatere dashboard når du skriver til mig i Telegram
- Sende beskeder tilbage med status
- Vise dashboard status når du beder om det

### ⚠️ Hvad der KRAÆVES for fuld integration:
- **Telegram Bot** - Skal oprettes af Mathias
- **Bot Token** - Fra BotFather
- **Chat ID** - Mathias skal finde sin Chat ID
- **Polling script** - Kører hver X minutter og tjekker Telegram

---

## 📝 SETUP - Trin for trin

### Trin 1: Opret Telegram Bot (Mathias gør dette!)

1. Åbn Telegram og søg efter **@BotFather**
2. Send `/newbot`
3. Vælg et navn (f.eks. `JueBot`)
4. Vælg brugernavn (f.eks. `jue_bot`)
5. **Gem BOT TOKEN!** (det ligner: `123456789:ABCdef...`)
6. Send `/setuserpic` hvis du vil have et billede på botten

### Trin 2: Få din Chat ID

**Metode A: Send en besked til botten**
1. Start scriptet: `python3 /root/clawd/dashboard/telegram-bot.py test`
2. Botten sender "🧪 Test besked fra Jue!"
3. Gå til denne URL: `https://api.telegram.org/bot<BOT_TOKEN>/getUpdates`
4. Du ser en JSON - find `"chat":{"id":123456789}`
5. Det tal er din **Chat ID**

**Metode B: Brug en test bot**
1. Åbn: https://t.me/userinfobot
2. Start botten og send "/start"
3. Den viser din Chat ID direkte!

### Trin 3: Konfigurer Jue

Opdater denne fil med dine credentials:

```python
TELEGRAM_TOKEN = "123456789:ABCdefGHI..."  # Fra BotFather
CHAT_ID = "123456789"  # Din Chat ID fra trin 2
```

---

## 💬 SÅDAN DU SKRIVER TIL JUE

### Format: Simpel og intuitivt!

```
Jue, todo: Læse Q4 rapporten
Jue, in-progress: Opdatere dokumentation
Jue, done: Læse færdig
Jue, status: Hvad er status?
Jue, hjælp: Hjælp mig med...
```

### Eksempler:

**Tilføj opgave:**
```
Mathias: Jue, todo: Gennemgå server logge
```
→ Jue opretter opgave i "To Do" ✅

**Start arbejde:**
```
Mathias: Jue, in-progress: Gennemgå server logge
```
→ Jue flytter til "Igangværende" og begynder at arbejde ⚡

**Mark som færdig:**
```
Mathias: Jue, done: Gennemgå server logge
```
→ Jue flytter til "Færdig" ✅

**Status tjek:**
```
Mathias: Jue, status
```
→ Jue sender dashboard status:

```
📋 To Do: 2 opgaver
⚡ Igangværende: 1 opgave
✅ Færdig: 0 opgaver
📱 Dashboard: http://147.79.102.93:3000
```

---

## 🔄 AUTOMATISK POLLING (VIGTIGT!)

Jue kan ikke selv tjekke Telegram - men et script kan!

### Opret polling script:

```bash
#!/bin/bash
# telegram-poll.sh - Kører hvert 2. minut

while true; do
    # Hent opdateringer fra Telegram
    UPDATES=$(curl -s https://api.telegram.org/bot<BOT_TOKEN>/getUpdates)

    # Parser og håndter kommandoer
    python3 /root/clawd/dashboard/telegram-handler.py "$UPDATES"

    # Vent 2 minutter
    sleep 120
done
```

### Eller brug cron:

```bash
# Kører hvert 2. minut
*/2 * * * * python3 /root/clawd/dashboard/telegram-handler.py
```

---

## 🎯 FULD WORKFLOW

### Matematias skriver til Jue i Telegram:
```
Mathias: Jue, todo: Læse Q4 rapporten
```

### Cron script tjekker Telegram hvert 2. minut:
- Finder "Jue, todo: Læse Q4 rapporten"
- Kalder python script
- Script opretter opgave i dashboard
- Script sender bekræftelse: "✅ Opgave oprettet: Læse Jue rapporten"

### Jue ser opgaven (automatisk eller manuel):
- Ser den i "To Do"
- Beslutter sig til at arbejde på den
- Flytter til "Igangværende"
- Begynder at arbejde (læser rapport, analyserer)
- Når færdig: Flytter til "Færdig"

### Matematias kan se alt på dashboardet:
- http://147.79.102.93:3000
- Opdaterer hvert 10 sekund!
- Kan se live status på sin telefon

---

## ⚠️ VIGTIGE BEGRÆNSNINGER

### Hvad Jue IKKE kan gøre:
- ❌ Læse Telegram uden at blive spurgt først
- ❌ Starte opgaver helt selv (jeg er ikke en selvstændig AI!)
- ❌ Tage beslutninger uden din godkendelse
- ❌ Polling på egen hånd (kræver script eller cron)

### Hvad Jue KAN gøre:
- ✅ Opdatere dashboard når du skriver i Telegram
- ✅ Sende statusbeskeder tilbage
- ✅ Finde opgaver selv i koden/logs/server
- ✅ Arbejde proaktivt når du har bedt om det
- ✅ Køre automatiske jobs (cron, sub-agents)

---

## 🚀 QUICK START (Når du har bot)

1. **Test botten:**
   ```bash
   python3 /root/clawd/dashboard/telegram-bot.py test
   ```

2. **Skriv din første opgave:**
   ```
   Mathias: Jue, todo: Test af Telegram integration
   ```

3. **Tjek dashboardet:**
   http://147.79.102.93:3000

---

## 🤔 HVORDAN JUE FINDER OPGAVER

Jue kan være proaktiv på disse måder:

### 1. Cron Jobs
```bash
# Hver dag kl 08:00
0 8 * * * /root/clawd/dashboard/daily-check.sh
```

Scriptet kan:
- Tjekke server logs for fejl
- Tjekke system status (CPU, memory, disk)
- Opdatere pakker
- Finde sikkerhedshuller
- Oprette opgaver automatisk

### 2. Fil Scanning
Jue kan scanne filer automatisk:
- `/var/log/` - Find nye fejl
- `/root/clawd/` - Find forbedringer
- Git repositories - Fundne nye commits

### 3. Sub-Agents
Jue kan spawnere sub-agenter der arbejder selvstændigt:
```bash
sessions_spawn task:"Analysér alle git repositories og find bugs"
sessions_spawn task:"Gennemgå system logs for fejl"
```

Sub-agenter rapporterer tilbage og Jue kan oprette opgaver!

---

## 🎯 SAMMENFATTENDE WORKFLOW

### Hverdage:
```
08:00 - Cron script kører og finder opgaver
        ↓
08:05 - Opgaver automatisk oprettet i "To Do"
        ↓
09:00 - Mathias skriver: "Jue, in-progress: Gennemgå logs"
        ↓
09:01 - Jue begynder at arbejde
        ↓
10:00 - Jue færdig: "Jue, done: Gennemgå logs"
        ↓
12:00 - Cleanup script kører: Sletter gamle færdige opgaver
```

### Nat (mens du sover):
```
02:00 - Proaktiv opgaver udføres
        ↓
06:00 - Mathias vågner til resultater på dashboardet
```

---

## 📱 KOMPLET KOMMANDO LISTE

```
Jue, todo: [title]           - Tilføj til To Do
Jue, in-progress: [title]    - Start arbejde
Jue, done: [title]           - Mark som færdig
Jue, status                      - Vis dashboard status
Jue, hjælp: [spørgsmål]    - Bed om hjælp
Jue, opdater: [status] [id] - Manuel opdatering
```

---

## 🎯 NÆSTE SKRIDT

1. **Opret Telegram bot** (@BotFather)
2. **Få din Chat ID** (@userinfobot eller via URL)
3. **Opdater credentials** i `/root/clawd/dashboard/telegram-bot.py`
4. **Test botten** med `python3 /root/clawd/dashboard/telegram-bot.py test`
5. **Skriv din første opgave:** `Jue, todo: Test integration`

---

## 💡 TIPS

- Vær tydelig med dine kommandoer
- Brug "Jue, " prefix for at tale til mig
- Tjek dashboardet ofte for status
- Brug "Jue, status" når du vil opdatere manuelt
- Lad cron scripts gøre det repetitive arbejde

---

## 🔐 SIKKERHED

- 🛡️ **Dine credentials er PRIVATE!** Del aldrig BOT TOKEN med andre
- 🔐 Brug kun sikre kanaler (privat med dig selv)
- ⚠️ Jue kan ikke læse beskeder fra andre brugere
- 🚫 Jue accepterer kun kommandoer fra din Chat ID

---

🎯 **Når du har sat det op, skriv:**
```
Mathias: Jue, status
```

Så bekræfter jeg at alt virker! 🧙‍♂️
