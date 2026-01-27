#!/usr/bin/env python3
# Codex CLI Integration - Auto-generer UI komponenter og features

import json
import sys
import subprocess
from pathlib import Path

WORKFLOW_AUTOMATOR_DIR = Path("/root/clawd/workflow-automator")
DASHBOARD_DIR = Path("/root/clawd/dashboard")

def run_codex(prompt, file_path=None, timeout=60):
    """Kører Codex CLI med givne prompt"""
    cmd = ["codex", "exec", prompt]
    if file_path:
        cmd.extend(["--file", str(file_path)])

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=WORKFLOW_AUTOMATOR_DIR
        )
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except subprocess.TimeoutExpired:
        return {"success": False, "error": "Codex CLI timeout"}
    except Exception as e:
        return {"success": False, "error": str(e)}

def generate_component(component_name, description, component_type="react"):
    """Generer en React komponent"""
    prompt = f"""Create a modern {component_type} component named {component_name} with this functionality: {description}.

Requirements:
- Use TypeScript with proper types
- If React, use functional components with hooks
- Use Tailwind CSS for styling
- Include error handling and loading states
- Make it responsive
- Add proper imports and exports
- Write clean, well-documented code

Return only the component code."""
    
    result = run_codex(prompt)
    return result

def generate_workflow_ui(workflow_name, workflow_type, custom_fields):
    """Generer custom workflow UI"""
    prompt = f"""Create a modern React TypeScript component for a {workflow_type} workflow UI.

Workflow Name: {workflow_name}
Custom Fields: {', '.join(custom_fields) if custom_fields else 'None'}

The UI should include:
1. Clean, modern design with Tailwind CSS
2. Form inputs for all custom fields with validation
3. Responsive layout (mobile and desktop)
4. Loading states and error handling
5. Submit and cancel buttons with proper styling
6. Integration with existing project structure

Use existing UI components if available (Card, Input, Button, etc.)
Write production-ready, well-documented code.

Return only the component code."""
    
    result = run_codex(prompt)
    return result

def fix_code(file_path, issue_description):
    """Ret en bug i en fil"""
    prompt = f"""Fix this issue in {file_path}: {issue_description}

Requirements:
- Keep the same structure and imports
- Only modify what's necessary to fix the bug
- Add comments explaining the fix
- Return the complete corrected file
- Ensure TypeScript types are correct

Return only the corrected code."""
    
    result = run_codex(prompt, file_path=str(file_path))
    return result

def generate_feature(feature_description, context=""):
    """Generer en ny feature"""
    prompt = f"""Implement this feature: {feature_description}

{f'Context: {context}' if context else ''}

Requirements:
- Write clean, maintainable code
- Include error handling
- Add TypeScript types
- Follow best practices
- Make it reusable if applicable
- Add comments for complex logic

Return only the code implementation."""
    
    result = run_codex(prompt)
    return result

def main():
    if len(sys.argv) < 2:
        print("🤖 Codex CLI Integration for Workflow Automator")
        print("")
        print("📝 KOMMANDOER:")
        print("  python3 codex-integration.py component <name> <description>")
        print("  python3 codex-integration.py workflow-ui <name> <type> [field1,field2,...]")
        print("  python3 codex-integration.py fix <file_path> <issue>")
        print("  python3 codex-integration.py feature <description> [context]")
        print("")
        print("📋 EKSEMPLER:")
        print("  python3 codex-integration.py component 'TodoFilter' 'Filter todos by status'")
        print("  python3 codex-integration.py workflow-ui 'EmailWorkflow' 'email' 'sender,subject,body'")
        print("  python3 codex-integration.py fix 'src/components/TodoItem.tsx' 'Todo does not toggle'")
        print("  python3 codex-integration.py feature 'Add drag and drop to todos' 'React DnD library available'")
        return 0

    command = sys.argv[1]

    if command == "component":
        if len(sys.argv) < 4:
            print("❌ Forventet: component <name> <description>")
            return 1
        name = sys.argv[2]
        description = ' '.join(sys.argv[3:])
        result = generate_component(name, description)
        print(json.dumps(result, indent=2))

    elif command == "workflow-ui":
        if len(sys.argv) < 4:
            print("❌ Forventet: workflow-ui <name> <type> [field1,field2,...]")
            return 1
        name = sys.argv[2]
        workflow_type = sys.argv[3]
        custom_fields = sys.argv[4].split(',') if len(sys.argv) > 4 else []
        result = generate_workflow_ui(name, workflow_type, custom_fields)
        print(json.dumps(result, indent=2))

    elif command == "fix":
        if len(sys.argv) < 4:
            print("❌ Forventet: fix <file_path> <issue>")
            return 1
        file_path = sys.argv[2]
        issue = ' '.join(sys.argv[3:])
        result = fix_code(file_path, issue)
        print(json.dumps(result, indent=2))

    elif command == "feature":
        if len(sys.argv) < 3:
            print("❌ Forventet: feature <description> [context]")
            return 1
        description = ' '.join(sys.argv[2:len(sys.argv)-1]) if len(sys.argv) > 3 else sys.argv[2]
        context = sys.argv[-1] if len(sys.argv) > 3 else ""
        result = generate_feature(description, context)
        print(json.dumps(result, indent=2))

    else:
        print(f"❌ Ukendt kommando: {command}")
        return 1

    return 0

if __name__ == '__main__':
    main()
