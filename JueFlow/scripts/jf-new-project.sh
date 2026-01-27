#!/bin/bash
# JueFlow New Project - Initialize new automated workflow project

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Directories
WORKSPACE="/root/clawd"
PLANNING_DIR="$WORKSPACE/.planning"
RESEARCH_DIR="$PLANNING_DIR/research"
PHASES_DIR="$PLANNING_DIR/phases"

# Ensure directories exist
mkdir -p "$PLANNING_DIR" "$RESEARCH_DIR" "$PHASES_DIR"

echo -e "${GREEN}🚀 JueFlow - New Project${NC}"
echo ""
echo "This will initialize a new project with:"
echo "  - Question-based requirements gathering"
echo "  - Automated domain research"
echo "  - Phased roadmap generation"
echo "  - Ready for autonomous overnight builds"
echo ""
echo -e "${YELLOW}Starting project initialization...${NC}"
echo ""

# This is a wrapper - actual work done by agent spawned via sessions_spawn
# The agent will use the JueFlow command templates

echo -e "${GREEN}✅ Planning directory structure created${NC}"
echo "  $PLANNING_DIR/"
echo "    ├── PROJECT.md (to be created by agent)"
echo "    ├── REQUIREMENTS.md (to be created by agent)"
echo "    ├── ROADMAP.md (to be created by agent)"
echo "    ├── STATE.md (to be created by agent)"
echo "    ├── research/"
echo "    └── phases/"
echo ""
echo -e "${YELLOW}⚡  Next: Run the project initialization agent${NC}"
echo "  This will ask questions, run research, and create all project files"
echo ""
echo -e "${GREEN}💡 Quick reference:${NC}"
echo "  /jf:new-project - Start new project"
echo "  /jf:discuss-phase N - Shape phase implementation"
echo "  /jf:plan-phase N - Create task plans"
echo "  /jf:execute-phase N - Build autonomously"
echo "  /jf:verify-work N - Confirm it works"
echo "  /jf:quick \"task\" - Ad-hoc task"
echo ""
