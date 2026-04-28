# Study Session Timer

A simple command-line Python application to track study sessions with a countdown timer, Pomodoro technique support, and logging.

## Features
- Start a timed study session with a subject.
- Visual progress bar during countdown.
- Pomodoro mode: 25-minute study sessions with 5-minute breaks, long breaks after 4 cycles.
- Logs sessions to a text file.
- View past study logs.

## Usage
1. Run the script: `python study_timer.py`
2. Choose option 1 to start a custom session.
3. Choose option 3 for Pomodoro mode.
4. Enter subject when prompted.
5. Wait for the timer or press Ctrl+C to stop early.
6. Choose option 2 to view logs.
7. Choose option 4 to exit.

## Requirements
- Python 3.x

## Troubleshooting
- Ensure Python is installed and in PATH.
- Logs are saved in `study_log.txt` in the same directory.
- If interrupted, the session is still logged with the intended duration.