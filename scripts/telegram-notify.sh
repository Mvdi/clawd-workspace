#!/bin/bash
# Telegram Notificering
# Bruger clawdbot message tool til at sende beskeder til Mathias

TITLE="$1"
CONTENT=$(cat)

# Send besked via clawdbot message tool
# Dette kaldes af Jue senere - scriptet er bare wrapper
echo "📤 Sending to Telegram: $TITLE"
