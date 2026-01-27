#!/bin/bash
# Weekly Learnings - Sender til Telegram
# Kører søndag kl 20:00 UTC (21:00 DK)

DATE=$(date +%Y-%m-%d)
OUTPUT_FILE="/root/clawd/weekly-learnings/${DATE}.md"

if [ -f "$OUTPUT_FILE" ]; then
    CONTENT=$(cat "$OUTPUT_FILE")

    # Send til Telegram
    echo "$CONTENT" | /root/.clawdbot/scripts/telegram-notify.sh "$DATE - Weekly Learnings" || true

    # Fallback hvis script ikke findes
    if [ $? -ne 0 ]; then
        echo "⚠️ Telegram script ikke fundet - vil bruge intern metode"
    fi
else
    echo "⚠️ Ingen weekly learnings fil fundet for $DATE"
fi
