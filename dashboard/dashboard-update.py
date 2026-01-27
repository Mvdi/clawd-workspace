#!/usr/bin/env python3
import json
import sys
from datetime import datetime, timezone

TASKS_FILE = "/root/clawd/dashboard/data/tasks.json"
ACTIVITY_FILE = "/root/clawd/dashboard/data/activity-log.json"
INFO_FILE = "/root/clawd/dashboard/data/dashboard-info.json"

def get_timestamp():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def log_activity(message):
    with open(ACTIVITY_FILE, 'r') as f:
        activity = json.load(f)

    timestamp = get_timestamp()
    new_id = activity[-1]['id'] + 1 if activity else 1

    new_entry = {
        "id": new_id,
        "message": message,
        "timestamp": timestamp
    }

    activity.append(new_entry)

    with open(ACTIVITY_FILE, 'w') as f:
        json.dump(activity, f, indent=2)

    print(f"✅ Logget: {message}")

def update_info():
    with open(INFO_FILE, 'r') as f:
        info = json.load(f)

    info['lastUpdated'] = get_timestamp()

    with open(INFO_FILE, 'w') as f:
        json.dump(info, f, indent=2)

def add_task(status, title, assignee="Jue", priority="medium"):
    with open(TASKS_FILE, 'r') as f:
        tasks = json.load(f)

    timestamp = get_timestamp()
    new_id = max([t['id'] for col in tasks.values() for t in col] + [0]) + 1

    column_map = {
        'todo': 'todo',
        'in-progress': 'in-progress',
        'done': 'done',
        'archived': 'archived'
    }

    column = column_map.get(status)
    if not column:
        print(f"❌ Invalid status: {status}")
        return False

    emoji_map = {
        'todo': '📋',
        'in-progress': '⚡',
        'done': '✅',
        'archived': '📦'
    }

    new_task = {
        "id": new_id,
        "title": title,
        "assignee": assignee,
        "created": timestamp,
        "priority": priority
    }

    if status == 'in-progress':
        new_task['updated'] = timestamp
    elif status == 'done':
        new_task['completed'] = timestamp

    tasks[column].append(new_task)

    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

    update_info()
    log_activity(f"{emoji_map[status]} {assignee}: {title} ({status})")
    return True

def move_task(task_id, new_status):
    with open(TASKS_FILE, 'r') as f:
        tasks = json.load(f)

    column_map = {
        'todo': 'todo',
        'in-progress': 'in-progress',
        'done': 'done',
        'archived': 'archived'
    }

    column = column_map.get(new_status)
    if not column:
        print(f"❌ Invalid status: {new_status}")
        return False

    # Find task i alle kolonner
    task = None
    source_col = None

    for col_name, col_tasks in tasks.items():
        for t in col_tasks:
            if t['id'] == task_id:
                task = t
                source_col = col_name
                break
        if task:
            break

    if not task:
        print(f"❌ Opgave {task_id} ikke fundet")
        return False

    # Fjern fra kilde kolonne
    tasks[source_col] = [t for t in tasks[source_col] if t['id'] != task_id]

    # Tilføj til ny kolonne
    tasks[column].append(task)

    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

    update_info()
    log_activity(f"🔄 Opgave {task_id} flyttet fra {source_col} til {column}")
    return True

def main():
    if len(sys.argv) < 2:
        print("🤖 Dashboard Updater (Python)")
        print("")
        print("Kommandoer:")
        print("  python3 dashboard-update.py log <message>")
        print("  python3 dashboard-update.py add <status> <title> [assignee] [priority]")
        print("  python3 dashboard-update.py move <id> <status>")
        print("  python3 dashboard-update.py update")
        print("")
        print("Eksempler:")
        print("  python3 dashboard-update.py log '🚀 Færdig med kode'")
        print("  python3 dashboard-update.py add todo 'Læse rapport' 'Mathias' høj")
        print("  python3 dashboard-update.py add in-progress 'Kode API' 'Jue'")
        print("  python3 dashboard-update.py add done 'Teste systemet' 'Jue'")
        print("  python3 dashboard-update.py move 1 done")
        print("  python3 dashboard-update.py update")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'log':
        if len(sys.argv) < 3:
            print("Usage: python3 dashboard-update.py log <message>")
            sys.exit(1)
        log_activity(sys.argv[2])
        update_info()

    elif command == 'add':
        if len(sys.argv) < 4:
            print("Usage: python3 dashboard-update.py add <status> <title> [assignee] [priority]")
            sys.exit(1)
        status = sys.argv[2]
        title = sys.argv[3]
        assignee = sys.argv[4] if len(sys.argv) > 4 else 'Jue'
        priority = sys.argv[5] if len(sys.argv) > 5 else 'medium'
        add_task(status, title, assignee, priority)

    elif command == 'move':
        if len(sys.argv) < 4:
            print("Usage: python3 dashboard-update.py move <id> <status>")
            sys.exit(1)
        task_id = int(sys.argv[2])
        new_status = sys.argv[3]
        move_task(task_id, new_status)

    elif command == 'update':
        update_info()
        log_activity("🔄 Dashboard opdateret")

    else:
        print(f"❌ Unknown command: {command}")
        sys.exit(1)

if __name__ == '__main__':
    main()
