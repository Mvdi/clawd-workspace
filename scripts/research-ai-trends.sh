#!/bin/bash
# Research AI Trends on X/Twitter
# Kører hver morgen kl 07:00 DK tid (06:00 UTC)
# Formål: Find nye AI tools, trends, og pain points fra rigtige developers

echo "🔍 Starting AI Trends Research..."
DATE=$(date +%Y-%m-%d)
OUTPUT_FILE="/root/clawd/memory/research-${DATE}.md"

cat << EOF > "$OUTPUT_FILE"
# AI Research Report - $DATE

## Trending Topics on X/Twitter
$(date)

EOF

echo "✅ Research template created. Jue vil fylde den ud via browser tool."
