import json
import time
from datetime import date
from pathlib import Path

LOG_FILE = Path(__file__).with_name("focus_log.json")


def print_menu():
    print("\nFocusTimer")
    print("1. Start a focus session")
    print("2. Show today's summary")
    print("3. Quit")
    print()


def print_summary(sessions):
    if not sessions:
        print("No focus sessions logged today")
        return

    totals = {}
    for session in sessions:
        name = session["name"]
        minutes = float(session["minutes"])
        totals[name] = totals.get(name, 0.0) + minutes

    grand_total = 0.0
    for name, total in totals.items():
        grand_total += total
        print(f"{name}: {total:.1f} min")

    print(f"Total: {grand_total:.1f} min")


def load_sessions():
    if not LOG_FILE.exists():
        return []

    try:
        with LOG_FILE.open("r", encoding="utf-8") as f:
            sessions = json.load(f)
    except (json.JSONDecodeError, OSError):
        return []

    if isinstance(sessions, list):
        return sessions
    return []


def save_sessions(sessions):
    with LOG_FILE.open("w", encoding="utf-8") as f:
        json.dump(sessions, f)


def start_focus_session():
    session_name = input("Enter a session name: ").strip()
    if not session_name:
        print("Session name cannot be empty.")
        return

    print(f"Focus session started for: {session_name}")
    start_time = time.time()
    input("Press Enter when you're done...")

    elapsed_seconds = time.time() - start_time
    minutes = round(elapsed_seconds / 60, 1)

    session = {
        "name": session_name,
        "date": date.today().isoformat(),
        "minutes": minutes,
    }

    sessions = load_sessions()
    sessions.append(session)
    save_sessions(sessions)

    print("Session finished.")


def show_summary():
    sessions = load_sessions()
    today = date.today().isoformat()
    todays_sessions = [session for session in sessions if session.get("date") == today]

    if not todays_sessions:
        print("No focus sessions logged today")
        return

    print_summary(todays_sessions)


def main():
    while True:
        print_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            start_focus_session()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()