#!/bin/bash
# Super simple dashboard updater - writes directly to files

TASKS_FILE="/root/clawd/dashboard/data/tasks.json"
ACTIVITY_FILE="/root/clawd/dashboard/data/activity-log.json"
INFO_FILE="/root/clawd/dashboard/data/dashboard-info.json"

get_timestamp() {
    date -u +"%Y-%m-%dT%H:%M:%SZ"
}

log_activity() {
    local msg="$1"
    local ts=$(get_timestamp)
    local id=$(cat "$ACTIVITY_FILE" | jq '.[-1].id // 0 + 1')

    local new_json=$(cat "$ACTIVITY_FILE" | jq --argjson new "[{\"id\":$id,\"message\":\"$msg\",\"timestamp\":\"$ts\"}]" '. + $new')
    echo "$new_json" > "$ACTIVITY_FILE"

    echo "✅ Logget: $msg"
}

update_info() {
    local ts=$(get_timestamp)
    local new_json=$(cat "$INFO_FILE" | jq --arg ts "$ts" '.lastUpdated = $ts')
    echo "$new_json" > "$INFO_FILE"
}

add_task() {
    local status="$1"
    local title="$2"
    local assignee="${3:-Jue}"
    local priority="${4:-medium}"
    local ts=$(get_timestamp)
    local new_id=$(cat "$TASKS_FILE" | jq '[.[].[] | .id] | max + 1')

    local new_task="{\"id\":$new_id,\"title\":\"$title\",\"assignee\":\"$assignee\",\"created\":\"$ts\",\"priority\":\"$priority\"}"

    if [ "$status" = "in-progress" ]; then
        new_task="{\"id\":$new_id,\"title\":\"$title\",\"assignee\":\"$assignee\",\"created\":\"$ts\",\"updated\":\"$ts\",\"priority\":\"$priority\"}"
    elif [ "$status" = "done" ]; then
        new_task="{\"id\":$new_id,\"title\":\"$title\",\"assignee\":\"$assignee\",\"created\":\"$ts\",\"completed\":\"$ts\",\"priority\":\"$priority\"}"
    fi

    local new_json=$(cat "$TASKS_FILE" | jq --argjson new "$new_task" --arg col "$status" '.[$col] += [$new]')
    echo "$new_json" > "$TASKS_FILE"

    update_info
    log_activity "📋 $assignee: $title ($status)"
}

move_task() {
    local task_id="$1"
    local new_status="$2"
    local ts=$(get_timestamp)

    # Find task i alle kolonner
    local task=$(cat "$TASKS_FILE" | jq --arg id "$task_id" '[.[].[] | select(.id == ($id | tonumber))][0]')

    if [ "$task" = "null" ] || [ -z "$task" ]; then
        echo "❌ Opgave $task_id ikke fundet"
        return 1
    fi

    # Fjern fra alle kolonner
    local temp_json=$(cat "$TASKS_FILE" | jq --arg id "$task_id" '
        .todo = [.todo[] | select(.id != ($id | tonumber))] |
        ."in-progress" = [."in-progress"[] | select(.id != ($id | tonumber))] |
        .done = [.done[] | select(.id != ($id | tonumber))] |
        .archived = [.archived[] | select(.id != ($id | tonumber))]
    ')

    # Tilføj opdateret task til ny kolonne
    local updated_task=$(echo "$task" | jq --arg ts "$ts" '.completed = ($ts)')
    local final_json=$(echo "$temp_json" | jq --argjson task "$updated_task" --arg col "$new_status" '.[$col] += [$task]')

    echo "$final_json" > "$TASKS_FILE"

    update_info
    log_activity "🔄 Opgave $task_id flyttet til $new_status"
}

# Main
case "$1" in
    log)
        if [ -z "$2" ]; then
            echo "Usage: $0 log <message>"
            exit 1
        fi
        log_activity "$2"
        update_info
        ;;
    add)
        if [ $# -lt 3 ]; then
            echo "Usage: $0 add <status> <title> [assignee] [priority]"
            echo "Status: todo, in-progress, done"
            exit 1
        fi
        add_task "$2" "$3" "$4" "$5"
        ;;
    move)
        if [ $# -lt 2 ]; then
            echo "Usage: $0 move <task_id> <status>"
            echo "Status: todo, in-progress, done, archived"
            exit 1
        fi
        move_task "$2" "$3"
        ;;
    update)
        update_info
        log_activity "🔄 Dashboard opdateret"
        ;;
    *)
        echo "🤖 Dashboard Updater"
        echo ""
        echo "Kommandoer:"
        echo "  $0 log <message>        - Log aktivitet"
        echo "  $0 add <status> <title>   - Tilføj opgave (todo/in-progress/done/archived)"
        echo "  $0 move <id> <status>   - Flyt opgave til kolonne"
        echo "  $0 update                  - Opdater dashboard timestamp"
        echo ""
        echo "Eksempler:"
        echo "  $0 log '🚀 Færdig med kode'"
        echo "  $0 add todo 'Læse rapport' 'Mathias' høj"
        echo "  $0 add in-progress 'Kode API' 'Jue'"
        echo "  $0 add done 'Teste systemet' 'Jue'"
        echo "  $0 move 1 done"
        exit 1
        ;;
esac
