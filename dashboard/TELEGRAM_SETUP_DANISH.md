# Telegram Setup Guide for Mathias & Sigrid

## Hvorfor to brugere?

Ja, I kan være to der bruger Telegram og snakker med mig! 📱

**Sådan virker det:**
- Én Telegram bot (én TOKEN)
- Hver bruger har sit eget Chat ID
- Systemet kender hvem der skriver og sender til rigtige huskeliste

---

## Step 1: Opret Telegram Bot (én gang)

1. Åbn Telegram og søg efter **@BotFather**
2. Start chat og skriv `/newbot`
3. Vælg et navn til din bot (f.eks. "Jue Task Manager")
4. Vælg et brugernavn (f.eks. "JueTaskManagerBot")
5. Kopier **TOKEN** du får fra BotFather

---

## Step 2: Find din Chat ID

Hver bruger skal finde deres eget Chat ID:

**For Mathias:**
1. Start en ny chat med din bot
2. Skriv en besked (f.eks. "hej")
3. Besøg: `https://api.telegram.org/bot<DIT_TOKEN>/getUpdates`
4. Find dit Chat ID i JSON svaret (se eksempel nedenfor)

**For Sigrid:**
- Sigrid skal gøre det samme
- Sigrid skal starte chat med botten
- Sigrid skal bruge samme link til at finde sit Chat ID

**Eksempel på svar fra getUpdates:**
```json
{
  "result": [
    {
      "message": {
        "from": {
          "id": 123456789,  ← Dette er Chat ID!
          "first_name": "Mathias"
        }
      }
    }
  ]
}
```

---

## Step 3: Konfigurer bot.py

Rediger `/root/clawd/dashboard/telegram-bot.py`:

```python
TELEGRAM_TOKEN = "din_bot_token_her"

CHAT_IDS = {
    "mathias": "mathias_chat_id_her",
    "sigrid": "sigrid_chat_id_her"
}
```

---

## Step 4: Test konfigurationen

```bash
cd /root/clawd/dashboard

# Test til Mathias
python3 telegram-bot.py test --user mathias

# Test til Sigrid
python3 telegram-bot.py test --user sigrid

# Test til alle
python3 telegram-bot.py test
```

---

## Step 5: Brug Telegram

Når konfiguration er færdig, kan I begge skrive til botten:

**Mathias:**
- "husk at købe mælk" → Tilføjes til Mathias' huskeliste
- "lav en rapport" → Tilføjes til Jue's opgaver

**Sigrid:**
- "husk at ringe til lægen" → Tilføjes til Sigrid's huskeliste
- "lav en analyse" → Tilføjes til Jue's opgaver

**Begge:**
- "status" → Se dashboard status (viser alle)

---

## Integration med Clawdbot

Når Clawdbot modtager beskeder fra Telegram, vil den automatisk:
1. Genkende hvem der skriver (fra Chat ID)
2. Kalde `telegram-bot.py` med `--user` parameter
3. Sende kvittering tilbage til den rigtige bruger

**Eksempel:**
```bash
# Mathias skriver: "husk at købe mælk"
python3 telegram-bot.py 'husk at købe mælk' --user mathias

# Sigrid skriver: "husk at ringe til lægen"
python3 telegram-bot.py 'husk at ringe til lægen' --user sigrid
```

---

## Dashboard

Se alle opgaver på http://147.79.102.93:3000

Dashboardet viser nu:
- 🧙‍♂️ Jue's opgaver
- 👤 Mathias' huskeliste
- 👩 Sigrid's huskeliste
- 📋 Projekt opgaver

Hver sektion har:
- Input felt til at tilføje nye todos
- Klik for at markere som færdig
- Slet-knap til at fjerne todos
- Real-time opdatering hvert 10 sekund

---

## CLI Kommandoer

```bash
# Tilføj todo til Mathias
python3 telegram-bot.py 'husk at købe mælk' --user mathias

# Tilføj todo til Sigrid
python3 telegram-bot.py 'husk at ringe til lægen' --user sigrid

# Bed Jue om at lave noget
python3 telegram-bot.py 'lav en rapport' --user mathias

# Se status for alle
python3 telegram-bot.py status

# Se status kun for Mathias
python3 telegram-bot.py status --user mathias
```

---

## Fejlfinding

**Ingen beskeder modtages:**
- Check at Chat IDs er korrekte
- Check at TOKEN er korrekt
- Tjek at både brugere har startet chat med botten

**Forkert bruger får besked:**
- Tjek at `--user` parameter er korrekt
- Verificer at Chat ID matcher rigtig person i `CHAT_IDS`

---

## Sikkerhed

- Del aldrig din BOT_TOKEN med andre
- Chat IDs er ikke hemmelige, men del dem ikke offentligt
- Bot skal være startet i Clawdbot for at modtage beskeder
