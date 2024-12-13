# simple-mac-terminal-reminder

A simple Python script that generates a timed reminder from your terminal. Creates a system notification using AppleScript (which will appear over other windows) once the time is up.

Just input a timer duration and message:

This can be via command line arguments:
```bash
# Just time (will prompt for message)
$ remind 15

# Time and message
$ remind 15m "Check the oven!"
```

Or an interactive prompt:
```bash
$ remind
Enter time (e.g., '5' for 5 minutes, '5m30s', '30s'): 15
Enter reminder message: Check the oven!
```

While the reminder is running, you'll see:
- A progress bar showing elapsed time
- Remaining time in MM:SS format
- Target completion time
- Terminal title updates with reminder info
- Controls reminder (Ctrl+C to cancel)

Example:
```
──────────────────────────────────────────────────────

🕰️  Reminder set at 10:30:15 AM for 15.0 minutes from now
⏰ Will ping at 10:45:15 AM
💬 Message: "Check the oven!"

─────────────── Controls ────────────────
Press Ctrl+C to cancel
──────────────────────────────────────────────────────

[██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 09:15 remaining (⏰ 10:45:15 AM)
```

## Installation

1. Clone the repo:
```bash
git clone https://github.com/Dillon-Z-Dong/simple-mac-terminal-reminder.git
```

2. Make the script executable:
```bash
chmod +x reminder.py
```

3. Set up the alias by adding this line to your `~/.zshrc`:
```bash
alias remind="python3 /full/path/to/reminder.py"
```
Replace `/full/path/to/` with the actual path to where you cloned the repository.

4. Reload your zsh configuration:
```bash
source ~/.zshrc
```

## Requirements
- macOS (uses AppleScript for notifications)
- Python 3.x