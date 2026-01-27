#!/usr/bin/env python3
# Simple task manager til at tilføje opgaver til Mathias

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
        'done': 'done'
    }

    column = column_map.get(status)
    if not column:
        print(f"❌ Invalid status: {status}")
        return False

    emoji_map = {
        'todo': '📋',
        'in-progress': '⚡',
        'done': '✅'
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

def main():
    if len(sys.argv) < 3:
        print("📋 Task Manager - Tilføj opgaver til Mathias")
        print("")
        print("Kommandoer:")
        print("  python3 add-task.py <status> <title>")
        print("")
        print("Status: todo, in-progress, done")
        print("")
        print("Eksempler:")
        print("  python3 add-task.py todo 'Læse rapport'")
        print("  python3 add-task.py in-progress 'Kode API'")
        print("  python3 add-task.py done 'Teste systemet'")
        sys.exit(1)

    status = sys.argv[1]
    title = sys.argv[2]

    assignee = "Mathias"
    priority = "medium"

    if len(sys.argv) > 3:
        assignee = sys.argv[3]
    if len(sys.argv) > 4:
        priority = sys.argv[4]

    print(f"📋 Tilføjer opgave...")
    add_task(status, title, assignee, priority)

if __name__ == '__main__':
    main()
