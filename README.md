# simple-mac-terminal-reminder
A python script (reminder.py) callable from the command line that creates a custom, timed MacOS system notification based on your inputs.

## Usage
### Setting a reminder
You can set reminders in two ways:

#### 1. Interactive prompt
```bash
$ remind
📋 Reminder Setup (Enter ➜ default, ? ➜ help)
Time (default ➜ 5m0s): 15
Message (default ➜ 15 minute reminder): Check the laundry!
Sound (default ➜ random): Purr
Volume (default ➜ normal): loud
```

Type `?` at any prompt to see available options and formats.

#### 2. Command line arguments
```bash
# Time and message
$ remind 15m "Check the laundry!"

# With sound and volume options
$ remind 15m "Check the laundry!" -s Purr -v loud
```

### Example Output
When you set a reminder, you'll see a progress display in your terminal:
```
──────────────────────────────────────────────────────
🕰️  Reminder set at 10:30:15 AM for 15m 00s from now
⏰ Will ping at 10:45:15 AM
💬 Message: "Check the laundry!"
🔊 Sound: Purr (Volume: loud)
─────────────── Controls ────────────────
Press Ctrl+C to cancel
──────────────────────────────────────────────────────

[██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 09:15 remaining (⏰ 10:45:15 AM)
```

When the timer completes, you'll see a popup which you can dismiss or snooze for 5 min:
```
╔══════════════ 🕰️ Reminder! ══════════════╗
║ ⌛️ 15m00s                                ║
║ 🕐 Current time: 10:45 AM                ║
║ 💤 Snoozed 2 times                       ║
║                                          ║
║ Check the laundry!                       ║
║                                          ║
║             [Got it] [+5 min]            ║
╚══════════════════════════════════════════╝
```

## Installation
Copy paste these commands in your terminal:

### Step 1: Create installation directory
```bash
echo -n "Enter installation directory (press Enter for default ~/.local/bin): "
read INSTALL_DIR
INSTALL_DIR="${INSTALL_DIR:-$HOME/.local/bin}"
mkdir -p "$INSTALL_DIR"
```

### Step 2: Download and configure the script
```bash
curl -s https://raw.githubusercontent.com/Dillon-Z-Dong/simple-mac-terminal-reminder/main/reminder.py > "$INSTALL_DIR/reminder.py"
chmod +x "$INSTALL_DIR/reminder.py"
```

### Step 3: Set up environment
```bash
echo -n "Enter alias name (press Enter for default 'remind'): "
read ALIAS_NAME
ALIAS_NAME="${ALIAS_NAME:-remind}"
echo -e "\n# Terminal Reminder\nexport PATH=\"\$PATH:$INSTALL_DIR\"\nalias $ALIAS_NAME=\"python3 $INSTALL_DIR/reminder.py\"" >> ~/.zshrc
source ~/.zshrc
```

### Step 4: Verify installation
```bash
echo "Installation complete! Script installed in $INSTALL_DIR. Try running: $ALIAS_NAME"
```

## Requirements
- macOS (uses AppleScript for notifications)
- Python 3.x

## Details

### Time Formats
- Minutes only: `5` or `5m`
- Seconds only: `30s`
- Minutes and seconds: `5m30s`
- Default: `5m0s`

### Sound Options
Available MacOS built-in sounds:
- Blow, Bottle, Frog, Funk, Glass, Hero
- Morse, Ping, Pop, Purr, Sosumi, Submarine, Tink
- Use `random` to let the system choose (default)

### Volume Levels
- `loud`: Maximum volume
- `normal`: Medium volume (default)
- `quiet`: Low volume
- `none`: Muted

### Command Line Arguments
```bash
usage: remind [-h] [-v {loud,normal,quiet,none}] [-s SOUND] [time] [message]

options:
  -h, --help            show this help message
  -v, --volume {loud,normal,quiet,none}
                        sound volume level
  -s, --sound {Blow,Bottle,Frog,Funk,Glass,Hero,Morse,Ping,Pop,Purr,Sosumi,Submarine,Tink,random}
                        sound effect to play
```

Examples with all options:
```bash
# Full example with all options
$ remind 5m30s "Check pizza in oven" -v loud -s Ping

# Interactive mode with help
$ remind
Time (default ➜ 5m0s): ?
Time can be specified in several formats:
- Minutes: 5 (same as 5m)
- Minutes and seconds: 5m30s
- Seconds only: 30s

# Using defaults with just a custom message
$ remind 10m "Give the bunnies a treat 🥕"
```