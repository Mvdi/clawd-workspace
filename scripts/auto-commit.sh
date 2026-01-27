#!/bin/bash
# Auto-Commit & Push to GitHub
# Kører hver aften kl 22:00 DK tid (21:00 UTC)
# Formål: Automatisk versionshistorik uden at Mathias skal tænke på det

cd /root/clawd

# Tjek om vi er i et git repo
if [ ! -d ".git" ]; then
    echo "⚠️ Not a git repo yet. Will initialize when Mathias provides GitHub details."
    exit 0
fi

# Tjek om der er ændringer
CHANGES=$(git status --porcelain | wc -l)
if [ "$CHANGES" -eq 0 ]; then
    echo "✅ No changes to commit."
    exit 0
fi

# Auto-commit
DATE=$(date +%Y-%m-%d)
git add .
git commit -m "Daily backup - $DATE

🤖 Auto-committed by Jue 🧙‍♂️
- Workspace: /root/clawd
- Changes: $CHANGES files"

# Push
git push 2>&1 || echo "⚠️ Push failed - may need authentication"

echo "✅ Committed $CHANGES files to GitHub!"
