#!/bin/bash
# Dashboard Management CLI

DATA_DIR="/root/clawd/dashboard/data"
TASKS_FILE="$DATA_DIR/tasks.json"
ACTIVITY_FILE="$DATA_DIR/activity-log.json"

add_activity() {
    local message="$1"
    local timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

    # Read current activities
    if [ -f "$ACTIVITY_FILE" ]; then
        activities=$(cat "$ACTIVITY_FILE")
    else
        activities="[]"
    fi

    # Add new activity
    new_id=$(echo "$activities" | jq '.[-1].id // 0 + 1')
    new_activity="{\"id\":$new_id,\"message\":\"$message\",\"timestamp\":\"$timestamp\"}"

    # Save updated activities
    echo "$activities" | jq ". + [$new_activity]" > "$ACTIVITY_FILE"
}

add_task() {
    local status="$1"  # todo, in-progress, done
    local title="$2"
    local assignee="$3"
    local priority="${4:-medium}"

    local timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    local column_name

    case "$status" in
        "todo") column_name="todo" ;;
        "in-progress") column_name="in-progress" ;;
        "done") column_name="done" ;;
        *)
            echo "❌ Invalid status: $status (use: todo, in-progress, done)"
            exit 1
            ;;
    esac

    # Generate new ID
    new_id=$(cat "$TASKS_FILE" | jq '[.[].[] | .id] | max + 1')

    # Build new task
    new_task="{\"id\":$new_id,\"title\":\"$title\",\"assignee\":\"$assignee\",\"created\":\"$timestamp\",\"priority\":\"$priority\"}"

    if [ "$status" = "in-progress" ]; then
        new_task=$(echo "$new_task" | jq ". + {\"updated\":\"$timestamp\"}")
    elif [ "$status" = "done" ]; then
        new_task=$(echo "$new_task" | jq ". + {\"completed\":\"$timestamp\"}")
    fi

    # Add to task list
    cat "$TASKS_FILE" | jq ".$column_name += [$new_task]" > "$TASKS_FILE.tmp"
    mv "$TASKS_FILE.tmp" "$TASKS_FILE"

    # Log activity
    local emoji="📋"
    [ "$status" = "in-progress" ] && emoji="⚡"
    [ "$status" = "done" ] && emoji="✅"

    add_activity "$emoji $assignee tilføjede opgave: $title"

    echo "✅ Opgave tilføjet til $column_name: $title"
}

move_task() {
    local task_id="$1"
    local new_status="$2"

    local column_name
    case "$new_status" in
        "todo") column_name="todo" ;;
        "in-progress") column_name="in-progress" ;;
        "done") column_name="done" ;;
        *)
            echo "❌ Invalid status: $new_status (use: todo, in-progress, done)"
            exit 1
            ;;
    esac

    # Find task and move it
    local task=$(cat "$TASKS_FILE" | jq ".[\"in-progress\"][] | select(.id == $task_id)" 2>/dev/null)
    if [ -z "$task" ]; then
        task=$(cat "$TASKS_FILE" | jq ".todo[] | select(.id == $task_id)" 2>/dev/null)
    fi
    if [ -z "$task" ]; then
        task=$(cat "$TASKS_FILES" | jq ".done[] | select(.id == $task_id)" 2>/dev/null)
    fi

    if [ -z "$task" ]; then
        echo "❌ Task with ID $task_id not found"
        exit 1
    fi

    # Remove from all columns and add to new column
    cat "$TASKS_FILE" | jq "
        .todo = [.todo[] | select(.id != $task_id)] |
        .[\"in-progress\"] = [.\"in-progress\"[] | select(.id != $task_id)] |
        .done = [.done[] | select(.id != $task_id)] |
        .$column_name += [$task]
    " > "$TASKS_FILE.tmp"
    mv "$TASKS_FILE.tmp" "$TASKS_FILE"

    echo "✅ Task $task_id moved to $column_name"
}

case "$1" in
    "add")
        if [ $# -lt 4 ]; then
            echo "Usage: $0 add <todo|in-progress|done> <title> <assignee> [priority]"
            exit 1
        fi
        add_task "$2" "$3" "$4" "$5"
        ;;
    "log")
        add_activity "$2"
        echo "✅ Aktivitet logget: $2"
        ;;
    "status")
        curl -s http://localhost:3000/api/tasks | jq
        ;;
    *)
        echo "🎯 Dashboard Management CLI"
        echo ""
        echo "Usage:"
        echo "  $0 add <todo|in-progress|done> <title> <assignee> [priority]"
        echo "  $0 log <message>"
        echo "  $0 status"
        echo ""
        echo "Examples:"
        echo "  $0 add todo 'Bygge ny feature' 'Jue' høj"
        echo "  $0 add done 'Teste systemet' 'Mathias'"
        echo "  $0 log '🚀 Server genstartet'"
        exit 1
        ;;
esac
