#!/usr/bin/env python3
# Telegram Task Manager - Modtager opgaver fra Mathias via Telegram

import json
import sys
import requests
from datetime import datetime, timezone

TELEGRAM_TOKEN = ""  # Mathias skal udfylde

# Brugere med deres Chat IDs
CHAT_IDS = {
    "mathias": "",  # Mathias skal udfylde
    "sigrid": ""    # Sigrid skal udfylde
}

# Navn mapping fra Chat ID til brugernavn
CHAT_ID_TO_USER = {v: k for k, v in CHAT_IDS.items() if v}

TASKS_FILE = "/root/clawd/dashboard/data/tasks.json"
ACTIVITY_FILE = "/root/clawd/dashboard/data/activity-log.json"
INFO_FILE = "/root/clawd/dashboard/data/dashboard-info.json"
PERSONAL_TODOS_FILE = "/root/clawd/dashboard/data/personal-todos.json"

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

def send_telegram_message(message, user=None):
    """Sender besked til bruger i Telegram
    
    Args:
        message: Besked der skal sendes
        user: Brugernavn ('mathias', 'sigrid', eller None for alle)
    """
    if not TELEGRAM_TOKEN:
        print("❌ Telegram ikke konfigureret")
        return False

    # Hvis ingen specifik bruger, send til alle
    if user is None:
        recipients = [(name, chat_id) for name, chat_id in CHAT_IDS.items() if chat_id]
    else:
        chat_id = CHAT_IDS.get(user)
        if not chat_id:
            print(f"❌ Chat ID for {user} ikke fundet")
            return False
        recipients = [(user, chat_id)]

    for recipient_name, chat_id in recipients:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "HTML"
        }

        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            print(f"📱 Telegram besked sendt til {recipient_name}: {message[:50]}...")
        except Exception as e:
            print(f"❌ Fejl ved Telegram til {recipient_name}: {e}")
            return False

    return True

def parse_personal_todo(text, person):
    """Parser tekst til personlig todo (husk/lav kommando)"""
    # Fjern "husk at" eller "lav" fra starten
    todo_text = text
    
    if text.lower().startswith('husk at '):
        todo_text = text[8:].strip()
    elif text.lower().startswith('husk '):
        todo_text = text[5:].strip()
    elif text.lower().startswith('lav '):
        todo_text = text[4:].strip()
    elif text.lower().startswith('jue, lav '):
        todo_text = text[10:].strip()
    
    return todo_text

def add_personal_todo(person, text, priority="medium"):
    """Tilføjer personlig todo"""
    with open(PERSONAL_TODOS_FILE, 'r') as f:
        personal = json.load(f)

    if person not in personal:
        personal[person] = []

    timestamp = get_timestamp()
    new_id = max([t['id'] for p in personal.values() for t in p] + [0]) + 1

    new_todo = {
        "id": new_id,
        "text": text,
        "priority": priority,
        "completed": False,
        "created": timestamp,
        "completedAt": None
    }

    personal[person].append(new_todo)

    with open(PERSONAL_TODOS_FILE, 'w') as f:
        json.dump(personal, f, indent=2)

    update_info()
    
    emoji = '🧙‍♂️' if person == 'jue' else '👤'
    activity_msg = f"{emoji} {person.capitalize()}: {text}"
    log_activity(activity_msg)
    
    return True

def show_dashboard_status(user=None):
    """Viser dashboard status for bruger eller alle
    
    Args:
        user: Brugernavn ('mathias', 'sigrid', eller None for alle)
    """
    with open(TASKS_FILE, 'r') as f:
        tasks = json.load(f)

    with open(PERSONAL_TODOS_FILE, 'r') as f:
        personal = json.load(f)

    # Beregn statistik
    jue_active = len([t for t in personal.get('jue', []) if not t['completed']])

    # Hvis specifik bruger, vis kun deres todos
    if user:
        user_personal = personal.get(user, [])
        user_active = len([t for t in user_personal if not t['completed']])
        user_top = [t for t in user_personal if not t['completed']][:3]

        user_todos_text = '\\n'.join([f'  • {t["text"]}' for t in user_top]) if user_top else ''

        status = f"""🎯 <b>Dashboard Status - {user.capitalize()}</b>

📋 <b>Projekt Opgaver:</b> {len(tasks.get('todo', []))} To Do | {len(tasks.get('in-progress', []))} Igang | {len(tasks.get('done', []))} Færdig

🧙‍♂️ <b>Jue's Opgaver:</b> {jue_active} aktive

👤 <b>{user.capitalize()}'s Huskeliste:</b> {user_active} aktive
{user_todos_text}

📱 <b>Tilgå dashboard:</b> http://147.79.102.93:3000
"""
        send_telegram_message(status, user=user)
    else:
        # Vis alle brugeres todos
        mathias_active = len([t for t in personal.get('mathias', []) if not t['completed']])
        sigrid_active = len([t for t in personal.get('sigrid', []) if not t['completed']])

        mathias_top = [t for t in personal.get('mathias', []) if not t['completed']][:2]
        sigrid_top = [t for t in personal.get('sigrid', []) if not t['completed']][:2]
        jue_top = [t for t in personal.get('jue', []) if not t['completed']][:2]

        jue_todos_text = '\\n'.join([f'  • {t["text"]}' for t in jue_top]) if jue_top else ''
        mathias_todos_text = '\\n'.join([f'  • {t["text"]}' for t in mathias_top]) if mathias_top else ''
        sigrid_todos_text = '\\n'.join([f'  • {t["text"]}' for t in sigrid_top]) if sigrid_top else ''

        status = f"""🎯 <b>Dashboard Status</b>

📋 <b>Projekt Opgaver:</b> {len(tasks.get('todo', []))} To Do | {len(tasks.get('in-progress', []))} Igang | {len(tasks.get('done', []))} Færdig

🧙‍♂️ <b>Jue's Opgaver:</b> {jue_active} aktive
{jue_todos_text}

👤 <b>Mathias' Huskeliste:</b> {mathias_active} aktive
{mathias_todos_text}

👩 <b>Sigrid's Huskeliste:</b> {sigrid_active} aktive
{sigrid_todos_text}

📱 <b>Tilgå dashboard:</b> http://147.79.102.93:3000
"""
        send_telegram_message(status)

    return True

def main():
    # Parse arguments
    import argparse
    parser = argparse.ArgumentParser(description='Telegram Task Manager for Jue')
    parser.add_argument('command', nargs='?', help='Kommando at udføre')
    parser.add_argument('--user', '-u', choices=['mathias', 'sigrid'], help='Bruger (hvis relevant)')
    args = parser.parse_args()

    if not args.command:
        print("📱 Telegram Task Manager")
        print("")
        print("📝 SETUP:")
        print("  1. Opret en Telegram bot: https://t.me/BotFather")
        print("  2. Hent token og sæt i denne fil")
        print("  3. Få din Chat ID og sæt i denne fil")
        print("")
        print("💬 KOMMANDOER:")
        print("  python3 telegram-bot.py 'husk [tekst]'                  → Tilføj til din huskeliste")
        print("  python3 telegram-bot.py 'husk [tekst]' --user sigrid    → Tilføj til Sigrid's huskeliste")
        print("  python3 telegram-bot.py 'lav [opgave]'                 → Tilføj til Jue's opgaver")
        print("  python3 telegram-bot.py 'jue, lav [opgave]'            → Tilføj til Jue's opgaver")
        print("  python3 telegram-bot.py status                         → Vis dashboard status (alle)")
        print("  python3 telegram-bot.py status --user mathias          → Vis status for Mathias")
        print("  python3 telegram-bot.py test                           → Test forbindelse (alle)")
        print("  python3 telegram-bot.py test --user sigrid             → Test forbindelse til Sigrid")
        return 0

    command = args.command
    user = args.user or 'mathias'  # Default til mathias hvis ingen bruger angivet

    if command == 'test':
        if user:
            send_telegram_message(f"🧪 Test besked fra Jue til {user.capitalize()}!", user=user)
        else:
            send_telegram_message("🧪 Test besked fra Jue!")
        return 0

    elif command == 'status':
        show_dashboard_status(user=user if user != 'mathias' else None)
        return 0

    # Personlige todos
    elif command.lower().startswith('husk '):
        todo_text = parse_personal_todo(command, user)
        if add_personal_todo(user, todo_text):
            send_telegram_message(f"✅ Tilføjet til {user.capitalize()}'s huskeliste: {todo_text}", user=user)
        return 0

    elif command.lower().startswith('lav '):
        todo_text = parse_personal_todo(command, 'jue')
        if add_personal_todo('jue', todo_text):
            # Send til den bruger der bedte om det
            send_telegram_message(f"✅ Tilføjet til Jue's opgaver: {todo_text}", user=user)
        return 0

    elif command.lower().startswith('jue, lav '):
        todo_text = parse_personal_todo(command, 'jue')
        if add_personal_todo('jue', todo_text):
            send_telegram_message(f"✅ Tilføjet til Jue's opgaver: {todo_text}", user=user)
        return 0

    else:
        # Fallback: Prøv at tolke som husk kommando
        todo_text = parse_personal_todo(command, user)
        if add_personal_todo(user, todo_text):
            send_telegram_message(f"✅ Tilføjet til {user.capitalize()}'s huskeliste: {todo_text}", user=user)
        else:
            send_telegram_message(f"❌ Ukendt kommando: {command}", user=user)
        return 1

if __name__ == '__main__':
    main()
