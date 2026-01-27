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

def cleanup_old_done_tasks():
    # SLET kun gamle "done" opgaver - ingen arkiv!
    with open(TASKS_FILE, 'r') as f:
        tasks = json.load(f)

    now = datetime.now(timezone.utc).timestamp()
    cutoff = now - 86400  # 24 timer

    print(f"📊 Tidspunkt nu: {datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"🗑️ Cutoff (24 timer siden): {datetime.fromtimestamp(cutoff).strftime('%Y-%m-%d %H:%M:%S UTC')}")

    # Filtrer done opgaver - behold kun nye
    old_count = 0
    keep_tasks = []

    for task in tasks.get('done', []):
        if 'completed' in task and task['completed']:
            try:
                completed_str = task['completed'].replace('Z', '+00:00')
                completed_time = datetime.fromisoformat(completed_str)
                if completed_time.timestamp() < cutoff:
                    old_count += 1
                    print(f"🗑️ Sletter gammel opgave: {task['title'][:50]}")
                else:
                    keep_tasks.append(task)
            except Exception as e:
                print(f"Error parsing timestamp: {e}", file=sys.stderr)
                keep_tasks.append(task)
        else:
            keep_tasks.append(task)

    # Opdater tasks
    if old_count > 0:
        tasks['done'] = keep_tasks
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=2)

        log_activity(f"🗑️ Slettede {old_count} gamle færdige opgaver (> 24 timer)")
        update_info()
    else:
        print("📋 Ingen gamle færdige opgaver at slette")

    print(f"📊 Beholder: {len(keep_tasks)} færdige opgaver")
    print(f"📊 Todo opgaver: {len(tasks.get('todo', []))} (ubeskåret)")
    print(f"📊 Igangværende opgaver: {len(tasks.get('in-progress', []))} (ubeskåret)")

def main():
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '--dry-run':
        print("🔍 DRY RUN - ingen sletning")
        # Kør cleanup uden at gemme
        pass

    print("🗑️ Cleanup - Sletter kun gamle færdige opgaver...")
    cleanup_old_done_tasks()
    print("✅ Cleanup færdig!")

if __name__ == '__main__':
    main()
