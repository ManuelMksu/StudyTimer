import time
import os
from datetime import datetime

def start_timer(minutes, subject, log_file):
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
    with open(log_file, 'a') as f:
        f.write(f"{end_time.strftime('%Y-%m-%d %H:%M:%S')} - {subject} - {minutes} minutes\n")
    print("Session logged.")

def view_logs(log_file):
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            logs = f.read()
        print("Study Logs:")
        print(logs if logs else "No logs yet.")
    else:
        print("No logs found.")

def start_pomodoro(subject, log_file):
    pomodoro_count = 0
    while True:
        # Work session
        print(f"\nStarting Pomodoro {pomodoro_count + 1} for '{subject}'.")
        start_timer(25, subject, log_file)
        pomodoro_count += 1
        
        # Break
        if pomodoro_count % 4 == 0:
            print("Time for a long break (15 minutes)!")
            start_timer(15, "Long Break", log_file)
        else:
            print("Short break (5 minutes).")
            start_timer(5, "Short Break", log_file)
        
        # Ask to continue
        cont = input("Continue with another Pomodoro? (y/n): ").strip().lower()
        if cont != 'y':
            break
    
    print(f"\nPomodoro session complete! Completed {pomodoro_count} Pomodoros.")
    # Log the session summary
    end_time = datetime.now()
    with open(log_file, 'a') as f:
        f.write(f"{end_time.strftime('%Y-%m-%d %H:%M:%S')} - {subject} - Pomodoro session: {pomodoro_count} completed\n")
    print("Session logged.")

def main():
    while True:
        username = input("Enter your username: ").strip()
        if username:
            break
        print("Username cannot be empty. Please try again.")
    
    log_file = f"{username}_study_log.txt"
    
    while True:
        print("\nStudy Session Timer")
        print("1. Start a study session")
        print("2. View logs")
        print("3. Start Pomodoro session")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            try:
                minutes = int(input("Enter session duration in minutes: "))
                subject = input("Enter subject: ").strip()
                if minutes > 0 and subject:
                    start_timer(minutes, subject, log_file)
                else:
                    print("Invalid input.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '2':
            view_logs(log_file)
        elif choice == '3':
            subject = input("Enter subject for Pomodoro: ").strip()
            if subject:
                start_pomodoro(subject, log_file)
            else:
                print("Invalid input.")
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()