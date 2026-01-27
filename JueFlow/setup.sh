#!/bin/bash
# JueFlow Setup - Install JueFlow into Clawdbot workspace

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

WORKSPACE="/root/clawd"
JUEFLOW_DIR="$WORKSPACE/JueFlow"

echo -e "${GREEN}🧙‍♂️ JueFlow - Automated Reliable Workflows${NC}"
echo ""
echo "Installing JueFlow into Clawdbot workspace..."
echo ""

# Copy commands to .claude/commands if exists, else local
if [ -d "$WORKSPACE/.claude/commands" ]; then
    CMD_DIR="$WORKSPACE/.claude/commands/jf"
else
    CMD_DIR="$JUEFLOW_DIR/commands"
    mkdir -p "$CMD_DIR"
fi

mkdir -p "$CMD_DIR"

# Copy command files
cp "$JUEFLOW_DIR/commands"/*.md "$CMD_DIR/" 2>/dev/null || true

echo -e "${GREEN}✅ Commands installed${NC}"
echo "  Location: $CMD_DIR"
echo ""
echo -e "${YELLOW}📁 Directory structure:${NC}"
echo "  $JUEFLOW_DIR/"
echo "    ├── README.md           # Full documentation"
echo "    ├── agents/              # Agent templates"
echo "    │   ├── jf-project-researcher.md"
echo "    │   ├── jf-planner.md"
echo "    │   ├── jf-executor.md"
echo "    │   ├── jf-verifier.md"
echo "    │   └── jf-debugger.md"
echo "    ├── commands/            # Command definitions"
echo "    │   ├── jf-new-project.md"
echo "    │   ├── jf-discuss-phase.md"
echo "    │   ├── jf-plan-phase.md"
echo "    │   ├── jf-execute-phase.md"
echo "    │   └── jf-verify-work.md"
echo "    └── scripts/             # Shell scripts"
echo "        ├── jf-new-project.sh"
echo "        ├── jf-discuss-phase.sh"
echo "        ├── jf-plan-phase.sh"
echo "        ├── jf-execute-phase.sh"
echo "        └── jf-verify-work.sh"
echo ""
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo -e "${YELLOW}📚 Next steps:${NC}"
echo "  1. Read: $JUEFLOW_DIR/README.md"
echo "  2. Initialize: /jf:new-project \"Your project idea\""
echo "  3. Build: /jf:execute-phase 1 (autonomous overnight builds)"
echo ""
echo -e "${GREEN}🚀 Ready to build reliable workflows!${NC}"
