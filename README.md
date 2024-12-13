# simple-mac-terminal-reminder

A simple Python script that creates timed reminders from your terminal.

## Features

- System notification pop-up when time expires. Appears over other windows.
- Interactive and command-line modes with flexible time input formats.
- Progress bar showing time remaining.
- Updates terminal title with reminder info.
- Can be cancelled with Ctrl+C.

## Installation

1. Clone the repository:
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

## Usage

### Interactive Mode
Simply type `remind` in your terminal and follow the prompts:

```bash
$ remind
Enter time (e.g., '5' for 5 minutes, '5m30s', '30s'): 15
Enter reminder message: Check the oven!
```

### Command Line Mode
You can pass arguments directly:

```bash
# Just time (will prompt for message)
$ remind 15

# Time and message
$ remind 15m "Check the oven!"
```

### Time Input Formats
The script accepts several time formats:
- Plain number (interpreted as minutes): `5`, `10`, `12.5`, etc.
- Minutes and seconds combined: `5m30s`
- Minutes only: `5m`
- Seconds only: `30s`

### Display Features
While the reminder is running, you'll see:
- A progress bar showing elapsed time
- Remaining time in MM:SS format
- Target completion time
- Terminal title updates with reminder info
- Controls reminder (Ctrl+C to cancel)

Example display:
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

## Requirements
- macOS (uses AppleScript for notifications)
- Python 3.x