#!/bin/bash
# Auto-Maintenance & Self-Improvement
# Kører hver søndag kl 03:00 DK tid (02:00 UTC)
# Formål: Hold mig opdateret, min hjerne organiseret, og find forbedringer

echo "🔧 Running weekly maintenance..."

# 1. Opdater system packages
echo "📦 Updating system..."
apt-get update -qq && apt-get upgrade -y -qq

# 2. Opdater npm packages
echo "📦 Updating npm..."
npm update -g clawdbot 2>/dev/null || true

# 3. Backup vigtige filer
echo "💾 Creating backups..."
mkdir -p /root/backups/weekly
tar -czf "/root/backups/weekly/clawd-backup-$(date +%Y-%m-%d).tar.gz" /root/clawd

# 4. Ryd gamle backups (>30 dage)
echo "🗑️ Cleaning old backups..."
find /root/backups/weekly -name "*.tar.gz" -mtime +30 -delete

# 5. Review memory files
echo "🧠 Reviewing memory..."
MEMORY_FILE="/root/clawd/MEMORY.md"
LAST_WEEK=$(date -d "7 days ago" +%Y-%m-%d)
TODAY=$(date +%Y-%m-%d)

echo -e "\n## Weekly Review - $(date)\n" >> "$MEMORY_FILE"
echo "### Vigtige ting ugen der gik:" >> "$MEMORY_FILE"
echo "TODO: Fyld ud når der er vigtige ting" >> "$MEMORY_FILE"

# 6. Check services
echo "🔍 Checking services..."
if systemctl is-active --quiet clawdbot-gateway; then
    echo "✅ Gateway running"
else
    echo "⚠️ Gateway NOT running - need attention!"
fi

echo "✅ Weekly maintenance complete!"
