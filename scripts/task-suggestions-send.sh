#!/bin/bash
# Task Suggestions - Sender til Telegram
# Kører kl 08:00 UTC (09:00 DK)

DATE=$(date +%Y-%m-%d)
OUTPUT_FILE="/root/clawd/suggestions/${DATE}.md"

# Hvis filen findes, send den
if [ -f "$OUTPUT_FILE" ]; then
    CONTENT=$(cat "$OUTPUT_FILE")

    # Send til Telegram
    echo "$CONTENT" | /root/.clawdbot/scripts/telegram-notify.sh "$DATE - Task Suggestions" || true

    # Fallback hvis script ikke findes
    if [ $? -ne 0 ]; then
        echo "⚠️ Telegram script ikke fundet - vil bruge intern metode"
    fi
else
    echo "⚠️ Ingen suggestions fil fundet for $DATE"
fi
