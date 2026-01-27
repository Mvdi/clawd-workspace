#!/usr/bin/env python3
# Jue's Morning Briefing System - autonomt finder opgaver og præsenterer dem

import json
import sys
import os
import subprocess
from datetime import datetime, timezone, timedelta

TASKS_FILE = "/root/clawd/dashboard/data/tasks.json"
ACTIVITY_FILE = "/root/clawd/dashboard/data/activity-log.json"
INFO_FILE = "/root/clawd/dashboard/data/dashboard-info.json"
DASHBOARD_URL = "http://147.79.102.93:3000"

# Telegram config - skal udfylles af Mathias!
TELEGRAM_TOKEN = ""  # Mathias skal udfylde
CHAT_ID = ""  # Mathias skal udfylde

def get_timestamp():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def log_activity(message):
    """Logger aktivitet"""
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
    """Opdaterer dashboard info"""
    with open(INFO_FILE, 'r') as f:
        info = json.load(f)

    info['lastUpdated'] = get_timestamp()

    with open(INFO_FILE, 'w') as f:
        json.dump(info, f, indent=2)

def get_system_status():
    """Henter system status (CPU, memory, disk)"""
    try:
        import psutil
        
        # CPU
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # Memory
        mem = psutil.virtual_memory()
        mem_usage = mem.percent
        mem_total = round(mem.total / (1024**3), 2)  # GB
        mem_used = round(mem.used / (1024**3), 2)  # GB
        
        # Disk
        disk = psutil.disk_usage('/')
        disk_usage = disk.percent
        disk_total = round(disk.total / (1024**3), 2)  # GB
        disk_used = round(disk.used / (1024**3), 2)  # GB
        
        status = {
            "cpu": cpu_usage,
            "memory": {"usage": mem_usage, "total_gb": mem_total, "used_gb": mem_used},
            "disk": {"usage": disk_usage, "total_gb": disk_total, "used_gb": disk_used}
        }
        
        return status, True
        
    except Exception as e:
        print(f"⚠️  Fejl ved system status: {e}", file=sys.stderr)
        return None, False

def check_git_status():
    """Tjekker git repositories for nye commits og bugs"""
    suggestions = []
    
    # Find alle git repos i /root/clawd/
    try:
        result = subprocess.run(
            ['find', '/root/clawd/', '-maxdepth', '2', '-type', 'd', '-name', '.git'],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print("⚠️  Kunne ikke finde git repos", file=sys.stderr)
            return []
            
        repos = result.stdout.strip().split('\n') if result.stdout.strip() else []
        
        for repo_git_dir in repos:
            if not repo_git_dir:
                continue
                
            repo_dir = os.path.dirname(repo_git_dir)
            
            # Tjek for nye commits (sidste 24 timer)
            try:
                since = datetime.now(timezone.utc) - timedelta(hours=24)
                since_str = since.strftime("%Y-%m-%dT%H:%M:%SZ")
                
                commit_result = subprocess.run(
                    ['git', '-C', repo_dir, 'log', '--since', since_str, '--oneline'],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                if commit_result.returncode == 0:
                    commits = commit_result.stdout.strip().split('\n')
                    recent_commits = [c for c in commits if c and c.strip()]
                    
                    if recent_commits:
                        suggestions.append({
                            "type": "git",
                            "priority": "medium",
                            "text": f"📚 {len(recent_commits)} nye commits i {os.path.basename(repo_dir)}"
                        })
                
            except Exception as e:
                print(f"⚠️  Fejl ved git tjek for {repo_dir}: {e}", file=sys.stderr)
        
        if suggestions:
            return suggestions
            
    except Exception as e:
        print(f"⚠️  Fejl ved git scanning: {e}", file=sys.stderr)
    
    return []

def check_logs_for_errors():
    """Scanner logs for fejl og problemer"""
    suggestions = []
    
    # Log steder at tjekke
    log_dirs = [
        '/var/log/',
        '/root/clawd/dashboard/',
        '/root/clawd/logs/'
    ]
    
    error_keywords = [
        'error', 'failed', 'exception', 'fatal', 'crash',
        'fejl', 'mislykkedes', 'timeout'
    ]
    
    for log_dir in log_dirs:
        if not os.path.exists(log_dir):
            continue
                
        try:
            log_files = os.listdir(log_dir)
        except Exception:
            continue
                
        for log_file in log_files:
            if not log_file.endswith('.log'):
                continue
                    
            log_path = os.path.join(log_dir, log_file)
            
            # Læs kun sidste 1000 linjer for performance
            try:
                with open(log_path, 'r', errors='ignore') as f:
                    lines = f.readlines()[-1000:]
                        
                    for line in lines:
                        line_lower = line.lower()
                        if any(keyword in line_lower for keyword in error_keywords):
                            suggestions.append({
                                "type": "log",
                                "priority": "high" if any(kw in ['fatal', 'crash', 'fejl'] for kw in error_keywords) else "medium",
                                "text": f"⚠️ Fejl i {log_file}: {line.strip()[:80]}"
                            })
                            break  # Kun én fejl per fil
                
            except Exception:
                continue
    
    return suggestions

def check_disk_space():
    """Tjekker disk plads"""
    suggestions = []
    
    try:
        import psutil
        disk = psutil.disk_usage('/')
        free_percent = 100 - disk.percent
        free_gb = round((disk.total - disk.used) / (1024**3), 2)
        
        if free_percent < 20:
            suggestions.append({
                "type": "system",
                "priority": "high",
                "text": f"⚠️ Disk plads lav! Kun {free_gb} GB ledig ({free_percent}%)"
            })
        elif free_percent < 40:
            suggestions.append({
                "type": "system",
                "priority": "medium",
                "text": f"💾 Disk plads okay: {free_gb} GB ledig ({free_percent}%)"
            })
    
    except Exception as e:
        print(f"⚠️  Fejl ved disk tjek: {e}", file=sys.stderr)
    
    return suggestions

def find_improvements_in_projects():
    """Finder forbedringer i projekt filer"""
    suggestions = []
    
    # Tjek for TODOs, FIXMEs, HACKs i koden
    try:
        result = subprocess.run(
            ['grep', '-r', '-n', '-E', '(TODO|FIXME|HACK|XXX)', '/root/clawd/', '--include=*.js', '--include=*.py', '--include=*.ts', '--include=*.tsx'],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0 and result.stdout.strip():
            matches = result.stdout.strip().split('\n')[:10]  # Max 10
            
            for match in matches:
                file, line, content = match.split(':')
                suggestions.append({
                    "type": "code",
                    "priority": "medium",
                    "text": f"🔧 {file}:{line}: {content.strip()}"
                })
    
    except Exception as e:
        print(f"⚠️  Fejl ved forbedrings tjek: {e}", file=sys.stderr)
    
    return suggestions

def add_task_to_dashboard(status, title, assignee="Jue", priority="medium"):
    """Tilføjer opgave til dashboard"""
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

def generate_morning_briefing():
    """Genererer den komplette morgen-briefing"""
    timestamp = get_timestamp()
    
    # Hent system status
    system_status, sys_ok = get_system_status()
    
    # Scan efter interessante opgaver
    suggestions = []
    
    # Tjekker...
    suggestions.extend(check_git_status())
    suggestions.extend(check_logs_for_errors())
    suggestions.extend(check_disk_space())
    suggestions.extend(find_improvements_in_projects())
    
    # Sorterer efter prioritet
    priority_order = {'high': 0, 'medium': 1, 'low': 2}
    suggestions.sort(key=lambda x: priority_order.get(x.get('priority', 'low'), 3))
    
    # Henter nuværende tasks fra dashboard
    try:
        with open(TASKS_FILE, 'r') as f:
            tasks = json.load(f)
    except Exception as e:
        print(f"⚠️  Fejl ved tasks: {e}", file=sys.stderr)
        tasks = {"todo": [], "in-progress": [], "done": []}
    
    # Genererer besked
    briefing_parts = []
    
    # Header
    briefing_parts.append("🌅 *JUE'S MORGENBRIEFING*")
    briefing_parts.append(f"📊 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    briefing_parts.append("")
    
    # System status
    if sys_ok and system_status:
        cpu = system_status['cpu']
        mem = system_status['memory']
        disk = system_status['disk']
        
        briefing_parts.append("🖥️  SYSTEM STATUS:")
        briefing_parts.append(f"   💻 CPU: {cpu}%")
        briefing_parts.append(f"   🧠 Memory: {mem['usage']:.1f}% ({mem['used_gb']}/{mem['total_gb']} GB)")
        briefing_parts.append(f"   💾 Disk: {disk['usage']:.1f}% ({disk['used_gb']}/{disk['total_gb']} GB)")
        briefing_parts.append("")
    
    # Aktuelle opgaver
    briefing_parts.append("📋 AKTUELLE OPGAVER:")
    
    if tasks.get('in-progress'):
        briefing_parts.append(f"   ⚡ Igangværende ({len(tasks['in-progress']))}:")
        for task in tasks['in-progress'][:3]:  # Max 3 i brevet
            briefing_parts.append(f"      - {task.get('title', 'Uden titel')}")
        briefing_parts.append("")
    
    if tasks.get('todo'):
        briefing_parts.append(f"   📋 To Do ({len(tasks['todo'])}):")
        for task in tasks.get('todo', [])[:3]:  # Max 3 i brevet
            briefing_parts.append(f"      - {task.get('title', 'Uden titel')}")
        briefing_parts.append("")
    
    briefing_parts.append("")
    
    # Forslag (hvis der er nogle)
    if suggestions:
        briefing_parts.append(f"💡 FORSLAG TIL DAGEN ({len(suggestions)}):")
        for suggestion in suggestions[:8]:  # Max 8 forslag
            priority_emoji = "🔴" if suggestion.get('priority') == 'high' else ("🟡" if suggestion.get('priority') == 'medium' else "🟢")
            briefing_parts.append(f"   {priority_emoji} {suggestion['text']}")
        briefing_parts.append("")
    else:
        briefing_parts.append("💡 Ingen særlige forslag - du bestemmer!")
        briefing_parts.append("")
    
    # Dashboard link
    briefing_parts.append("📱 DASHBOARD:")
    briefing_parts.append(f"   {DASHBOARD_URL}")
    briefing_parts.append("")
    
    # Footer
    briefing_parts.append("🎯 Hav en produktiv dag! - Jue")
    
    briefing_text = "\n".join(briefing_parts)
    
    return briefing_text, suggestions

def send_telegram_message(text):
    """Sender besked til Telegram"""
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("❌ Telegram ikke konfigureret - se TOPEN af denne fil")
        return False
    
    try:
        import requests
        
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = {
            "chat_id": CHAT_ID,
            "text": text,
            "parse_mode": "HTML"
        }
        
        response = requests.post(url, json=data)
        response.raise_for_status()
        print(f"📱 Telegram besked sendt ({len(text)} tegn)")
        return True
    except Exception as e:
        print(f"❌ Fejl ved Telegram: {e}", file=sys.stderr)
        return False

def add_tasks_to_dashboard(suggestions):
    """Tilføjer fundne forslag som opgaver til dashboard hvis de er vigtige"""
    if not suggestions:
        return
    
    # Tilføj kun HIGH priority forslag automatisk
    high_priority = [s for s in suggestions if s.get('priority') == 'high']
    
    if not high_priority:
        return
    
    # Log activity
    with open(ACTIVITY_FILE, 'r') as f:
        activity = json.load(f)
    
    timestamp = get_timestamp()
    new_id = activity[-1]['id'] + 1 if activity else 1
    
    for suggestion in high_priority:
        new_entry = {
            "id": new_id,
            "message": f"🔍 Autonomorning briefing fundet: {suggestion['text']}",
            "timestamp": timestamp
        }
        activity.append(new_entry)
        new_id += 1
    
    with open(ACTIVITY_FILE, 'w') as f:
        json.dump(activity, f, indent=2)
    
    # Tilføj til tasks
    with open(TASKS_FILE, 'r') as f:
        tasks = json.load(f)
    
    task_id = max([t['id'] for col in tasks.values() for t in col] + [0]) + 1
    
    for suggestion in high_priority:
        new_task = {
            "id": task_id,
            "title": suggestion['text'],
            "assignee": "Mathias",
            "created": timestamp,
            "priority": "high"
        }
        tasks['todo'].append(new_task)
        task_id += 1
    
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)
    
    # Update info
    with open(INFO_FILE, 'r') as f:
        info = json.load(f)
    info['lastUpdated'] = timestamp
    with open(INFO_FILE, 'w') as f:
        json.dump(info, f, indent=2)
    
    print(f"✅ Tilføjede {len(high_priority)} højprioriterede opgaver til dashboard")

def main():
    """Hovedfunktion"""
    if len(sys.argv) < 2:
        print("🌅 Jue's Morning Briefing System")
        print("")
        print("📝 SETUP:")
        print("  1. Opret en Telegram bot: https://t.me/BotFather")
        print("  2. Få BOT TOKEN og sæt i denne fil")
        print("  3. Få din CHAT ID og sæt i denne fil")
        print("")
        print("📋 BRUG:")
        print("  python3 morning-briefing.py              - Kører morgen-briefing nu")
        print("  python3 morning-briefing.py test       - Tester systemet")
        print("")
        print("⚙️  CRON (automatisk hver dag kl 08:00):")
        print("  0 8 * * * python3 /root/clawd/dashboard/morning-briefing.py >> /root/clawd/dashboard/morning-briefing.log 2>&1")
        print("")
        print("📱 Telegram kommandoer i denne chat:")
        print("  Jue, status           - Se dashboard status")
        print("  Jue, help             - Vis denne hjælp")
        return 0
    
    command = sys.argv[1]
    
    if command == 'test':
        print("🧪 Tester systemet...")
        print("")
        
        # Test psutil
        try:
            import psutil
            print(f"✅ psutil version: {psutil.__version__}")
            print(f"💻 CPU: {psutil.cpu_percent()}%")
            print(f"🧠 Memory: {psutil.virtual_memory().percent}%")
            print(f"💾 Disk: {psutil.disk_usage('/').percent}%")
        except Exception as e:
            print(f"❌ Fejl ved psutil test: {e}")
        
        # Test tasks fil
        try:
            with open(TASKS_FILE, 'r') as f:
                print(f"✅ Tasks fil: OK")
        except Exception as e:
            print(f"❌ Fejl ved tasks: {e}")
        
        print("")
        print("🎉 Systemtest færdig!")
        return 0
    
    elif command == 'status':
        # Vis dashboard status via Telegram
        try:
            with open(TASKS_FILE, 'r') as f:
                tasks = json.load(f)
            
            status = f"""
📊 <b>Dashboard Status</b>

📋 <b>To Do:</b> {len(tasks.get('todo', []))}
⚡ <b>Igangværende:</b> {len(tasks.get('in-progress', []))}
✅ <b>Færdig:</b> {len(tasks.get('done', []))}

📱 <b>Tilgå dashboard:</b> {DASHBOARD_URL}
"""
            
            send_telegram_message(status)
            return 0
        except Exception as e:
            print(f"❌ Fejl ved status: {e}", file=sys.stderr)
            return 1
    
    elif command == 'help':
        print("📚 Jue's Morning Briefing System - Hjælp")
        print("")
        print("📋 KOMMANDOER:")
        print("  python3 morning-briefing.py          - Kører morgen-briefing nu")
        print("  python3 morning-briefing.py test       - Tester systemet")
        print("  python3 morning-briefing.py status     - Sender dashboard status til Telegram")
        print("")
        print("📱 TELEGRAM:")
        print("  Skriv følgende i denne chat:")
        print("    Jue, status - Se dashboard status")
        print("    Jue, help   - Vis denne hjælp")
        print("")
        print("📊 SYSTEM CHECKS:")
        print("  🖥️  System status (CPU, Memory, Disk)")
        print("  📚  Git commits i sidste 24 timer")
        print("  ⚠️  Logs for fejl og problemer")
        print("  💾  Disk plads kontrol")
        print("  🔧  Kode forbedringer (TODO, FIXME, HACK)")
        print("")
        print("⚙️  SETUP:")
        print("  1. Opret Telegram bot via @BotFather")
        print("  2. Få BOT TOKEN og sæt i denne fil (TELEGRAM_TOKEN)")
        print("  3. Få din CHAT ID og sæt i denne fil (CHAT_ID)")
        print("  4. Tilføj cron: 0 8 * * * python3 /root/clawd/dashboard/morning-briefing.py")
        return 0
    
    # Kør morgen-briefing
    print("🌅 Genererer morgen-briefing...")
    briefing_text, suggestions = generate_morning_briefing()
    
    # Tilføj højprioriterede forslag som opgaver
    add_tasks_to_dashboard(suggestions)
    
    # Send til Telegram
    send_success = send_telegram_message(briefing_text)
    
    if send_success:
        print("✅ Morgen-briefing sendt!")
    else:
        print("❌ Kunne ikke sende til Telegram")
    
    # Log activity
    with open(ACTIVITY_FILE, 'r') as f:
        activity = json.load(f)
    
    timestamp = get_timestamp()
    new_id = activity[-1]['id'] + 1 if activity else 1
    
    new_entry = {
        "id": new_id,
        "message": "🌅 Morgen-briefing sendt til Mathias",
        "timestamp": timestamp
    }
    
    activity.append(new_entry)
    
    with open(ACTIVITY_FILE, 'w') as f:
        json.dump(activity, f, indent=2)
    
    # Update dashboard info
    with open(INFO_FILE, 'r') as f:
        info = json.load(f)
    info['lastUpdated'] = timestamp
    with open(INFO_FILE, 'w') as f:
        json.dump(info, f, indent=2)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"❌ Kritisk fejl: {e}", file=sys.stderr)
        sys.exit(1)
