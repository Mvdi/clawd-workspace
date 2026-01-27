# 🎯 Dashboard Guide - Sådan vi samarbejder!

## 📱 Dashboard URL
**http://147.79.102.93:3000**

Du kan se det fra din Mac eller telefon!

---

## 🎮 3 VIGTIGE KOLONNER

| Kolonne | Hvad det betyder | Status |
|---------|------------------|--------|
| **📋 To Do** | Opgaver der skal gøres | Nogen arbejder på dem |
| **⚡ Igangværende** | Hvad jeg arbejder på **NU** | Aktiv fokus her |
| **✅ Færdig** | Completed opgaver | Slettes automatisk efter 24 timer |

---

## 1. 💬 HVORDAN DU OPRETTER OPGAVER TIL MIG

### Metode A: Skrive besked til mig (ENKELT!)

Bare skriv til mig i denne chat:

```
Jue, lav en opgave: Læse rapporten fra Q4
```

Så opretter jeg en opgave og begynder at arbejde på den!

### Metode B: Via chat (mere detaljeret)

```
Mathias: "Tilføj opgave til Jue: Opdatere dokumentation om dashboardet"
Jue: ✅ Opgave tilføjet til "To Do": "Opdatere dokumentation om dashboardet"
```

### Metode C: Eksplicit status

```
Jue, start på dette: Byg en login formular
Mathias: ✅ Starter nu - opgaven er i "Igangværende"
```

---

## 2. 🔄 HVORDAN VI SAMARBEJDER (WORKFLOW)

### Eksempel 1: Læse rapport

```
Mathias: "Jue, læs Q4 rapporten og opsummer vigtige punkter"
Jue: ✅ Opgave i "To Do" - begynder at læse...
[5 minutter senere]
Jue: ✅ Færdig! Rapporten har 3 vigtige punkter. Gemt i /root/clawd/reports/q4-summary.md
```

### Eksempel 2: Bygge feature

```
Mathias: "Jue, byg en funktion der validerer emails"
Jue: ✅ Opgave i "To Do" - analyserer krav...
[10 minutter senere]
Jue: ⚡ Flytter til "Igangværende" - koder nu...
[15 minutter senere]
Jue: ✅ Færdig! Funktionen er i /root/clawd/myapp/email-validator.js
```

### Eksempel 3: Proaktivt arbejde (jeg finder selv opgaver)

```
Jue: 📊 Jeg har fundet 3 bugs i koden der bør fixes
Jue: ✅ Opgaver tilføjet til "To Do":
   - Fix memory leak i auth.js
   - Optimize database queries
   - Add error handling til API
```

---

## 3. 🧠 HVORDAN JEG FINDER OPGAVER

### Metode A: Du beder mig
```
Mathias: "Tjek alle nye commits og fix bugs"
Jue: ✅ Fundet 2 commits med bugs - tilføjer til To Do
```

### Metode B: Jeg er proaktiv
```
Jue: 📋 Jeg scanner filer og finder opgaver
Jue: ✅ Fundet 5 forbedringer - opretter opgaver
```

### Metode C: Cron jobs / tidspunkt
```
# Jeg kører script hver dag kl 08:00 der tjekker:
# - Nye emails
# - Calendar events
# - System status
# Og opretter opgaver automatisk!
```

---

## 4. 📊 STATUS FLOW

### To Do → Igangværende
```
Mathias: "Start på opgaven nu"
Jue: ✅ Flytter opgaven til "Igangværende"
```

### Igangværende → Færdig
```
Jue: ⚡ Arbejder på opgaven...
Jue: ✅ Færdig! Flytter til "Færdig"
```

### Færdig → Slettet (24 timer senere)
```
# Automatisk cleanup script kører
# Fjerner alle færdige opgaver > 24 timer
```

---

## 5. 🤖 HVORDAN DU KAN FØLGE MED

### Se hvad jeg laver nu
- Åbn dashboardet
- Kig i "Igangværende" kolonnen
- Der ser du hvad jeg arbejder på **NU**

### Se hvad jeg har lavet
- Kig i "Færdig" kolonnen
- Eller se "Aktivitetslog" nederst
- Du ser de sidste 20 handlinger

### Start en ny opgave
- Bare skriv til mig!
- Eksempel: "Jue, analyserer server loggen"
- Jeg opretter den og begynder at arbejde

---

## 6. 🎯 PRAKTISKE EKSEMPLER

### Eksempel 1: Daglig rutine
```
Mathias (morgen): "Goddag! Her er dagens opgaver:"
Mathias: "1. Tjek emails"
Mathias: "2. Opdater dashboard"
Mathias: "3. Gennemgå nye commits"

Jue: ✅ Opretter opgaver og begynder arbejdet
```

### Eksempel 2: Projektarbejde
```
Mathias: "Jeg vil gerne have en ny feature til appen"
Mathias: "Bruger skal kunne uploade billeder"

Jue: ✅ Opgave i To Do - analyserer requirements
Jue: ⚡ Igangværende - designer upload flow
Jue: ⚡ Igangværende - implementerer backend
Jue: ✅ Færdig - Upload feature er klar! 📸
```

### Eksempel 3: Fejlfinding
```
Mathias: "Der er en bug i login systemet"
Mathias: "Nogle gange logger man ikke ind"

Jue: ✅ Opgave i To Do - debugger login
Jue: ⚡ Igangværende - læser logs
Jue: ✅ Færdig - Fundet og fixet bugen! 🐛
```

---

## 7. 🌙 NATLIG ARBEJDE

Jeg kan arbejde mens du sover! Sig til hvis du vil have det:

**Muligheder:**
```
Mathias: "Jeg vil gerne have at du kører code review hver nat"
Mathias: "Hver morgen kl 07:00 vil jeg have en opsummering"
```

**Så gør jeg:**
```
# Cron job hver nat kl 02:00
python3 /root/clawd/dashboard/cleanup.sh

# Sub-agent der arbejder selvstændigt
sessions_spawn task:"Læs alle emails, opsummer vigtige"
```

---

## 8. 📱 FRA DIN MAC

### Åbn dashboardet
```
Safari eller Chrome: http://147.79.102.93:3000
```

### Se i realtid
- Dashboardet opdaterer hver 10 sekund
- Du ser alt hvad jeg laver live!

---

## 9. ⚠️ HVIS NOGET IKKE VIRKER

### Aktivitetslog viser ikke?
- Vent 10 sekunder - den opdaterer automatisk
- Refresh browseren

### Dashboardet viser ikke opdaterede data?
- Det sker hvert 10 sekund - vær tålmodig

---

## 🎯 HURTIG START

**Prøv nu:**
```
Jue, lav en simpel opgave: Hej verden
```

Så ser du mig:
1. ✅ Oprette opgaven
2. ⚡ Flytte den til "Igangværende"
3. ✅ Flytte den til "Færdig"

**Alt i realtid på dashboardet!** 📱
