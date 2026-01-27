# 🎯 OpenCode CLI & Coding Agent - Status

## ✅ Installeret og Klar!

### OpenCode CLI (v1.1.36)
**Status:** ✅ Installeret, testet og virker!

**Kommando:**
```bash
opencode --version
# 1.1.36
```

**Test:**
- ✅ Læser filer
- ✅ Skriver filer (ramte rate limit - men det er normalt!)
- ✅ Dansk sprogunderstøttelse

---

## 🧩 Coding Agent Skill - Aktiveret!

Du har nu adgang til 3 coding agents:

### 1. OpenCode (Hovedagent)
```bash
# Interaktiv - hurtige opgaver
bash pty:true workdir:/path/to/project command:"opencode --model openai/gpt-4o run 'Lav en login funktion'"

# Background - lange opgaver
bash pty:true workdir:/path/to/project background:true command:"opencode --model openai/gpt-4o-mini run 'Byg en REST API'"
```

### 2. Pi Coding Agent (Alternativ)
```bash
bash pty:true workdir:/path/to/project command:"pi 'Lav en funktion der...'"

# Kræver ikke model parameter - bruger standarden
```

### 3. Claude Code (Kræver API key)
```bash
bash pty:true workdir:/path/to/project command:"claude 'Byg...'"
```

---

## 📋 Model Valg (Vigtigt!)

### OpenCode Modeller
```bash
opencode models  # Se alle tilgængelige modeller
```

**Anbefalede:**
- `openai/gpt-5-codex` - **Bedst til koding**
- `openai/gpt-4o-mini` - Hurtig og billig
- `openai/gpt-5` - Nyeste og kraftigste

**Rate Limits:**
- GPT-4o har rate limits (30000 TPM)
- Brug `gpt-4o-mini` eller `gpt-5-codex` for mindre begrænsninger

---

## 🎮 Eksempler

### Eksempel 1: Lav en ny funktion
```bash
cd ~/my-project
opencode --model openai/gpt-5-codex run "Lav en funktion der validerer email addresses"
```

### Eksempel 2: Fix en bug
```bash
cd ~/my-project
opencode --model openai/gpt-4o-mini run "Der er en bug i src/utils.js linje 45. Fix den."
```

### Eksempel 3: Refaktor kode
```bash
cd ~/my-project
bash pty:true workdir:/path/to/project background:true \
  command:"opencode --model openai/gpt-5-codex run 'Refaktor auth modulet for bedre performance'"
```

### Eksempel 4: Build et projekt
```bash
cd ~/new-project
git init
opencode --model openai/gpt-5 run "Byg en simpel to-do app med HTML, CSS og JavaScript"
```

---

## 📊 Monitor Running Sessions

```bash
# List alle kørende sessions
process action:list

# Se output fra en session
process action:log sessionId:XXX

# Check status
process action:poll sessionId:XXX

# Stop en session
process action:kill sessionId:XXX
```

---

## 🔧 Opsætning

### OpenCode konfiguration
```bash
opencode auth            # Håndter credentials
opencode stats           # Se token usage og costs
```

### Model konfiguration
```bash
# Sæt default model
export OPENAI_MODEL_NAME=openai/gpt-5-codex

# Eller brug --model flag hver gang
opencode --model openai/gpt-5-codex run "..."
```

---

## ⚠️ Husk!

1. **Brug altid `pty:true`** for coding agents (som i eksemplerne)
2. **Start i en git repo** - coding agents arbejder bedst der
3. **Vælg rigtig model** - gpt-5-codex er bedst til koding
4. **Brug background mode** for lange opgaver
5. **Monitor sessions** med `process action:log`

---

## 🎯 Næste Skridt?

Prøv at køre en lille opgave nu:

```bash
cd /tmp/test
git init && echo "# Test" > README.md
opencode --model openai/gpt-5-codex run "Lav en index.html med Hello World"
```

Sig til hvis du vil have mig til at køre en test eller hjælpe med et projekt! 🧙‍♂️
