import time
import os
from datetime import datetime

LOG_FILE = 'study_log.txt'

def start_timer(minutes, subject):
    total_seconds = minutes * 60
    print(f"Starting {minutes}-minute study session for '{subject}'.")
    print("Press Ctrl+C to stop early.")

    try:
        for i in range(total_seconds, 0, -1):
            mins, secs = divmod(i, 60)
            progress = (total_seconds - i) / total_seconds * 100
            bar = '#' * int(progress // 10) + '-' * (10 - int(progress // 10))
            print(f"\r[{bar}] {mins:02d}:{secs:02d} remaining", end='', flush=True)
            time.sleep(1)
        print("\nSession complete!")
    except KeyboardInterrupt:
        print("\nSession stopped early.")

    # Log the session
    end_time = datetime.now()
    with open(LOG_FILE, 'a') as f:
        f.write(f"{end_time.strftime('%Y-%m-%d %H:%M:%S')} - {subject} - {minutes} minutes\n")
    print("Session logged.")

def view_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            logs = f.read()
        print("Study Logs:")
        print(logs if logs else "No logs yet.")
    else:
        print("No logs found.")

def main():
    while True:
        print("\nStudy Session Timer")
        print("1. Start a study session")
        print("2. View logs")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            try:
                minutes = int(input("Enter session duration in minutes: "))
                subject = input("Enter subject: ").strip()
                if minutes > 0 and subject:
                    start_timer(minutes, subject)
                else:
                    print("Invalid input.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '2':
            view_logs()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()