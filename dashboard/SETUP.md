# Jue & Mathias Dashboard - Setup Guide

## ✅ Dashboard er klar!

Dit dashboard kører nu på **http://147.79.102.93:3000**

### Hjemmenetværk
Fra din computer eller telefon på samme netværk kan du tilgå det via:
- `http://147.79.102.93:3000`

---

## 📱 Adgang udefra (når du ikke er hjemme)

Her er 3 muligheder - vælg den der passer dig bedst:

### 1. Tailscale VPN ⭐️ (Anbefalet - gratis & nemt)
**Hvorfor:** Sikker, privat, fungerer overalt uden port forwarding.

**På din server (jeg kan gøre det):**
```bash
tailscale up
```
Det giver dig en login-link. Log ind med din Google/GitHub konto.

**På din telefon:**
1. Download Tailscale app (iOS/Android)
2. Log ind med samme konto
3. Åbn appen og klik på din server
4. Tilknyttet URL: `http://100.x.x.x:3000` (Tailscale IP)

---

### 2. SSH Tunneling (Teknisk, men kræver ingen konto)
**På din telefon:**
1. Download Termux (Android) eller Prompt/iShell (iOS)
2. Kør: `ssh -L 3000:localhost:3000 din-bruger@147.79.102.93`
3. Åbn browser: `http://localhost:3000`

**Hvorfor det virker:** Tunnel forwarder port 3000 fra serveren til din telefon.

---

### 3. Cloudflare Tunnel (Kræver Cloudflare konto)
Jeg har downloadet cloudflared - hvis du vil bruge dette, så sig til så sætter jeg det op.

---

## 🎮 Dashboard Features

### 3 Kolonner:
- **📋 To Do** - Opgaver der skal gøres
- **⚡ Igangværende** - Hvad jeg arbejder på nu
- **✅ Færdig** - Hvad der er completed

### Aktivitetslog:
- Se hvad jeg har lavet og hvornår
- Automatisk opdatering hvert 10. sekund

### Mobilvenligt:
- Responsivt design
- Mørkt tema (godt om natten)
- Touch-venlig

---

## 🔧 API Endpoints (hvis du vil bygge på)

```bash
GET /api/tasks      # Alle opgaver
GET /api/activity   # Aktivitetslog
GET /api/info       # Dashboard info
```

Data lagres i JSON filer i `data/` mappen - du kan redigere dem direkte hvis du vil.

---

## 🚀 Server Status

- **Port:** 3000
- **Status:** Kører ✅
- **IP:** 147.79.102.93

For at stoppe serveren:
```bash
pkill -f "node server.js"
```

For at starte igen:
```bash
cd /root/clawd/dashboard && node server.js &
```

---

## 💡 Næste skridt

Vælg en adgangsmetode og sig til - jeg hjælper dig med setup!

Jeg anbefaler **Tailscale** hvis du vil have det nemt og sikkert.
