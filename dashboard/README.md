# 🧙‍♂️ Jue & Mathias Dashboard

Projektstyring for AI-assistent og human samarbejde.

## 🚀 Quick Start

Dashboardet kører på: **http://147.79.102.93:3000**

Fra din telefon (hjemme): Samme URL
Fra din telefon (ude): Se [SETUP.md](SETUP.md) for adgangsmuligheder

---

## 📱 Features

- **3-kolonne kanban board** - To Do / Igangværende / Færdig
- **Aktivitetslog** - Se hvad der er sket og hvornår
- **Mobilvenligt design** - Responsive, touch-venlig
- **Dark mode** - Godt for øjnene, især om aftenen
- **Auto-refresh** - Opdateres hvert 10. sekund
- **JSON-baseret data** - Nemt at redigere eller automatisere

---

## 🛠️ Teknologi

- **Frontend:** HTML + CSS + Vanilla JavaScript
- **Backend:** Node.js + Express
- **Data:** JSON filer (ingen database krævet)
- **Deployment:** Systemd service (autostart)

---

## 📂 Struktur

```
/root/clawd/dashboard/
├── index.html           # Frontend UI
├── server.js            # Express backend
├── manage.sh            # CLI management tool
├── data/
│   ├── tasks.json       # Opgaver i 3 kolonner
│   ├── activity-log.json # Aktivitetslog
│   └── dashboard-info.json # Dashboard metadata
├── README.md            # Denne fil
├── SETUP.md             # Opsætningsguide
└── BRUGERGUIDE.md       # Brugervejledning
```

---

## 🎮 Kommandoer

### Start/Stop dashboard
```bash
# Start
systemctl start dashboard

# Stop
systemctl stop dashboard

# Restart
systemctl restart dashboard

# Status
systemctl status dashboard
```

### Tilføj opgaver
```bash
# Via CLI
./manage.sh add <todo|in-progress|done> <title> <assignee> [priority]

# Via mig (Mathias)
"Jue, tilføj en opgave til To Do: Læse rapport"
```

### Log aktivitet
```bash
./manage.sh log "🚀 Server genstartet"
```

### Se status
```bash
./manage.sh status
# Eller besøg http://147.79.102.93:3000
```

---

## 🎨 Eksempel opgaver

```json
{
  "todo": [
    {
      "id": 1,
      "title": "Opsæt ekstern adgang til dashboard",
      "assignee": "Mathias",
      "created": "2026-01-26T17:00:00Z",
      "priority": "høj"
    }
  ],
  "in-progress": [
    {
      "id": 2,
      "title": "Bygge Jue & Mathias projekt-dashboard",
      "assignee": "Jue",
      "created": "2026-01-26T17:00:00Z",
      "updated": "2026-01-26T17:00:00Z",
      "priority": "høj"
    }
  ],
  "done": [
    {
      "id": 3,
      "title": "Designe UI",
      "assignee": "Jue",
      "created": "2026-01-26T17:00:00Z",
      "completed": "2026-01-26T17:00:00Z",
      "priority": "medium"
    }
  ]
}
```

---

## 🔐 Sikkerhed

Dashboardet kører på port 3000. For ekstern adgang anbefales:
- **Tailscale VPN** - Privat, sikker, ingen port forwarding
- **Cloudflare Tunnel** - Gratis, nemt
- **SSH tunneling** - Teknisk, men kræver ingen konto

Se [SETUP.md](SETUP.md) for detaljer.

---

## 💡 Fremtidige forbedringer

Idéer til senere:
- [ ] Brugerlogin / authentication
- [ ] Real-time WebSockets updates
- [ ] Push notifikationer ved nye opgaver
- [ ] Tags/kategorier på opgaver
- [ ] Due dates og reminders
- [ ] Kommentarer på opgaver
- [ ] Fil-upload vedhæftninger
- [ ] Backup/restore af data

Sig til hvis du vil have nogle af disse! 🧙‍♂️

---

## 📞 Support

Problemer eller idéer? Sig til - jeg er klar til at hjælpe!
