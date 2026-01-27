#!/bin/bash
# Dashboard Auto-Update Helper - Simplified version using API

DASHBOARD_API="http://localhost:3000/api"
TASKS_FILE="/root/clawd/dashboard/data/tasks.json"
ACTIVITY_FILE="/root/clawd/dashboard/data/activity-log.json"
INFO_FILE="/root/clawd/dashboard/data/dashboard-info.json"

# Helper functions
get_timestamp() {
    date -u +"%Y-%m-%dT%H:%M:%SZ"
}

log_activity() {
    local message="$1"
    local timestamp=$(get_timestamp)
    local id=$(cat "$ACTIVITY_FILE" | jq '.[-1].id // 0 + 1')

    jq --arg id "$id" \
       --arg msg "$message" \
       --arg ts "$timestamp" \
       '. + [{id: ($id | tonumber), message: $msg, timestamp: $ts}]' "$ACTIVITY_FILE" > "$ACTIVITY_FILE.tmp"
    mv "$ACTIVITY_FILE.tmp" "$ACTIVITY_FILE"

    echo "✅ Logget: $message"
}

update_dashboard_info() {
    local last_updated=$(get_timestamp)
    jq --arg ts "$last_updated" '.lastUpdated = $ts' "$INFO_FILE" > "$INFO_FILE.tmp"
    mv "$INFO_FILE.tmp" "$INFO_FILE"
}

add_task() {
    local status="$1"
    local title="$2"
    local assignee="${3:-Jue}"
    local priority="${4:-medium}"

    local timestamp=$(get_timestamp)
    local column_name
    local emoji

    case "$status" in
        "todo")
            column_name="todo"
            emoji="📋"
            ;;
        "in-progress")
            column_name="in-progress"
            emoji="⚡"
            ;;
        "done")
            column_name="done"
            emoji="✅"
            ;;
        *)
            echo "❌ Invalid status: $status"
            return 1
            ;;
    esac

    local new_id=$(cat "$TASKS_FILE" | jq '[.[].[] | .id] | max + 1')

    # Read current tasks
    local current_tasks=$(cat "$TASKS_FILE")

    # Build new task JSON properly
    local new_task_json
    if [ "$status" = "in-progress" ]; then
        new_task_json=$(echo "[$current_tasks]" | jq --argjson new "{\"id\":$new_id,\"title\":\"$title\",\"assignee\":\"$assignee\",\"created\":\"$timestamp\",\"updated\":\"$timestamp\",\"priority\":\"$priority\"}" \
           --arg col "$column_name" \
           '.[$col] += [$new]')
    elif [ "$status" = "done" ]; then
        new_task_json=$(echo "[$current_tasks]" | jq --argjson new "{\"id\":$new_id,\"title\":\"$title\",\"assignee\":\"$assignee\",\"created\":\"$timestamp\",\"completed\":\"$timestamp\",\"priority\":\"$priority\"}" \
           --arg col "$column_name" \
           '.[$col] += [$new]')
    else
        new_task_json=$(echo "[$current_tasks]" | jq --argjson new "{\"id\":$new_id,\"title\":\"$title\",\"assignee\":\"$assignee\",\"created\":\"$timestamp\",\"priority\":\"$priority\"}" \
           --arg col "$column_name" \
           '.[$col] += [$new]')
    fi

    echo "$new_task_json" | jq '.' > "$TASKS_FILE"

    update_dashboard_info
    log_activity "$emoji $assignee: $title"
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
            echo "❌ Invalid status: $new_status"
            return 1
            ;;
    esac

    # Find and move task
    cat "$TASKS_FILE" | jq "
        .todo = [.todo[] | select(.id != ($task_id | tonumber))] |
        .\"in-progress\" = [.\"in-progress\"[] | select(.id != ($task_id | tonumber))] |
        .done = [.done[] | select(.id != ($task_id | tonumber))] |
        .[\"$column_name\"] += ([.todo[] + [.\"in-progress\"[]] + [.done[]]] | select(.id == ($task_id | tonumber)))
    " > "$TASKS_FILE.tmp"
    mv "$TASKS_FILE.tmp" "$TASKS_FILE"

    update_dashboard_info
    log_activity "🔄 Opgave $task_id flyttet til $column_name"
}

# Main command handler
case "$1" in
    "log")
        if [ -z "$2" ]; then
            echo "Usage: $0 log <message>"
            exit 1
        fi
        log_activity "$2"
        update_dashboard_info
        ;;
    "add")
        if [ $# -lt 3 ]; then
            echo "Usage: $0 add <status> <title> [assignee] [priority]"
            exit 1
        fi
        add_task "$2" "$3" "$4" "$5"
        ;;
    "update")
        update_dashboard_info
        log_activity "🔄 Dashboard opdateret"
        ;;
    *)
        echo "🤖 Jue's Dashboard Auto-Update Helper"
        echo ""
        echo "Kommandoer:"
        echo "  $0 log <message>        - Log aktivitet"
        echo "  $0 add <status> <title>   - Tilføj opgave (todo/in-progress/done)"
        echo "  $0 update                  - Opdater dashboard timestamp"
        echo ""
        echo "Eksempler:"
        echo "  $0 log '🚀 Færdig med kode'"
        echo "  $0 add todo 'Læse rapport' 'Mathias' høj"
        echo "  $0 add in-progress 'Kode API' 'Jue'"
        echo "  $0 add done 'Teste systemet' 'Jue'"
        exit 1
        ;;
esac
