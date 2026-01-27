# Jue & Mathias Dashboard - Brugerguide

## 🎯 Kom i gang

Dashboardet er dit projektstyringsværktøj - et sted hvor vi kan se hvad der skal gøres, hvad der sker nu, og hvad der er færdigt.

### Åbn dashboardet
- Fra din computer: http://147.79.102.93:3000
- Fra din telefon (hjemme): Samme URL
- Fra din telefon (ude): Se SETUP.md for adgangsmuligheder

---

## 📋 De 3 Kolonner

### 📋 To Do
Opgaver der skal gøres - enten af mig eller dig.

### ⚡ Igangværende
Hvad der bliver arbejdet på lige nu. Max 1-2 opgaver her ad gangen.

### ✅ Færdig
Completed opgaver. Godt at kigge tilbage på for at se fremskridt!

---

## 🛠️ Sådan bruger du det

### Vis dashboard
```bash
# I din terminal eller via mig:
curl http://147.79.102.93:3000
```

### Tilføj opgave
Du kan bede mig om det, eller bruge CLI:
```bash
/root/clawd/dashboard/manage.sh add <status> <title> <assignee> [priority]

# Eksempler:
/root/clawd/dashboard/manage.sh add todo "Læse rapport" "Mathias" høj
/root/clawd/dashboard/manage.sh add in-progress "Skrive kode" "Jue"
/root/clawd/dashboard/manage.sh add done "Teste feature" "Mathias"
```

### Log aktivitet
```bash
/root/clawd/dashboard/manage.sh log "🚀 Server genstartet"
/root/clawd/dashboard/manage.sh log "💡 Fik ny idé til projektet"
```

### Se status via CLI
```bash
/root/clawd/dashboard/manage.sh status
```

---

## 💡 Bedste praksis

### Opgavetitler
- Vær specifik: "Skrive kode" → "Implementere brugerlogin endpoint"
- Brug aktivt sprog: "Gøre noget" → "Gøre noget"

### Prioriteter
- **høj:** Må gøres i dag/nærmeste fremtid
- **medium:** Bør gøres inden for en uge
- **lav:** Kan vente

### Hvornår bruger du hvad?
- **To Do:** Nye idéer, opgaver du vil huske
- **Igangværende:** Max 2-3 opgaver ad gangen
- **Færdig:** Når en opgave er helt done, flyt den hertil

---

## 🤝 Samarbejde

### Hvordan jeg bruger det
- Jeg flytter automatisk opgaver mellem kolonnerne
- Jeg logger min aktivitet så du kan følge med
- Jeg kan foreslå opgaver til dig hvis det giver mening

### Hvordan du bruger det
- Tilføj opgaver du vil huske (Jeg kan også gøre det for dig!)
- Se hvad jeg arbejder på - du behøver ikke spørge
- Flyt opgaver til "Færdig" når du er done

### Proaktivitet
- Hvis du ser en opgave der mangler, sig til eller tilføj den
- Hvis noget står i "Igangværende" for længe, spørg om hjælp
- Følg med i aktivitetsloggen for at se hvad jeg har lavet

---

## 🔄 Automatisk opdatering

Dashboardet opdaterer sig selv hvert 10. sekund, så du altid ser nyeste tilstand uden at skulle refresh.

---

## 🚨 Problemer?

### Dashboard svarer ikke
```bash
# Tjek om serveren kører
systemctl status dashboard

# Restart hvis nødvendigt
systemctl restart dashboard
```

### Kan ikke tilgå fra telefonen
- Er du på samme netværk? Hvis nej, se SETUP.md
- Er port 3000 blokeret? Check firewall

### Data ser forkert ud
Data ligger i `/root/clawd/dashboard/data/` - du kan redigere JSON filerne direkte, men vær forsigtig!

---

## 📞 Hjælp

Har du spørgsmål eller idéer til forbedringer? Sig til - jeg er her for at hjælpe! 🧙‍♂️
