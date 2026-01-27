#!/bin/bash
# Competitive Intelligence - Sender til Telegram
# Kører tirsdag/fredag kl 10:00 UTC (11:00 DK)

DATE=$(date +%Y-%m-%d)
OUTPUT_FILE="/root/clawd/competitive-intel/${DATE}.md"

if [ -f "$OUTPUT_FILE" ]; then
    CONTENT=$(cat "$OUTPUT_FILE")

    # Send til Telegram
    echo "$CONTENT" | /root/.clawdbot/scripts/telegram-notify.sh "$DATE - Competitive Intel" || true

    # Fallback hvis script ikke findes
    if [ $? -ne 0 ]; then
        echo "⚠️ Telegram script ikke fundet - vil bruge intern metode"
    fi
else
    echo "⚠️ Ingen competitive intel fil fundet for $DATE"
fi
