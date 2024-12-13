# simple-mac-terminal-reminder

A simple Python script that allows you to generate a custom MacOS system notification which will display after an input time. The reminder runs in a terminal and can be cancelled with Ctrl+C.

## Usage
- Input a timer duration and reminder message

Via an interactive prompt:
```bash
$ remind
Enter time (e.g., '5' for 5 minutes, '5m30s', '30s'): 15
Enter reminder message: Check the oven!
```

or command line arguments:
```bash
# Just time (will prompt for message)
$ remind 15

# Time and message
$ remind 15m "Check the oven!"
```

This will create a display in your terminal with a progress bar:
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

Copy and paste these commands into your terminal:

```bash
# Choose installation directory (default: ~/.local/bin)
read -p "Enter installation directory (press Enter for default ~/.local/bin): " INSTALL_DIR
INSTALL_DIR="${INSTALL_DIR:-$HOME/.local/bin}"

# Create directory if it doesn't exist
mkdir -p "$INSTALL_DIR"

# Download the reminder script
curl -s https://raw.githubusercontent.com/Dillon-Z-Dong/simple-mac-terminal-reminder/main/reminder.py > "$INSTALL_DIR/reminder.py"

# Make the script executable
chmod +x "$INSTALL_DIR/reminder.py"

# Add to PATH and create alias in your shell configuration
echo -e "\n# Terminal Reminder\nexport PATH=\"\$PATH:$INSTALL_DIR\"\nalias remind=\"python3 $INSTALL_DIR/reminder.py\"" >> ~/.zshrc

# Reload shell configuration
source ~/.zshrc

# Confirm installation
echo "Installation complete! Script installed in $INSTALL_DIR. Try running: remind"
```

## Requirements
- macOS (uses AppleScript for notifications)
- Python 3.x