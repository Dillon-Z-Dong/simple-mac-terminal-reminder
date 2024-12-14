# simple-mac-terminal-reminder
A command line tool that creates a custom, timed MacOS system notification based on your inputs.

## Two ways to set a reminder:

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

## Reminder Display:

Once your reminder is set, the terminal will show a progress bar + reminder details. You can cancel the reminder at any time with Ctrl+C.

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

When the timer completes, your sound will play, and you'll get a popup with options to dismiss or snooze (+5 min). Snoozing will launch another ```reminder``` instance in the same tab, and the number of snoozes will tracked in the display/popup.

```
╔══════════════ 🕰️ Reminder! ══════════════╗
║ ⌛️ 15m00s                                ║
║ 🕐 Current time: 10:45 AM                ║
║ 💤 Snoozed 1 time                        ║
║                                          ║
║ Check the laundry!                       ║
║                                          ║
║             [Got it] [+5 min]            ║
╚══════════════════════════════════════════╝
```

## Requirements
- macOS (with any Python 3.x installation, e.g., the OS default)

## Installation

Copy paste these lines in your terminal:

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

## More usage examples:

Quick time + message input:
```bash
$ remind 15m "Check pizza in oven"
```

Command line with all options:
```bash
$ remind 10m30s "Give the bunnies a treat 🥕" -v quiet -s Funk
```

Interactive mode with help:
```bash
$ remind
──────────────────────────────────────────────────
📋 Reminder Setup (Enter ➜ default, ? ➜ help)
──────────────────────────────────────────────────
Time (default ➜ 5m0s): ?

Time can be specified in several formats:
- Minutes: 5 (same as 5m)
- Minutes and seconds: 5m30s
- Seconds only: 30s
        
Time (default ➜ 5m0s): 2m30s
──────────────────────────────────────────────────
Message (default ➜ 2m 30s reminder): ?

Enter any text you would like to see when the reminder pops up.
        
Message (default ➜ 2m 30s reminder): 🐰🐰🐰
──────────────────────────────────────────────────
Sound (default ➜ random): ?

Available sounds: Blow, Bottle, Frog, Funk, Glass, Hero, Morse, Ping, Pop, Purr, Sosumi, Submarine, Tink
Enter 'random' to let the system choose one for you.
        
Sound (default ➜ random): frog
──────────────────────────────────────────────────
Volume (default ➜ normal): ?

Volume levels:
- loud: Maximum volume
- normal: Medium volume
- quiet: Low volume
- none: Muted
        
Volume (default ➜ normal):       
──────────────────────────────────────────────────

──────────────────────────────────────────────────

🕰️  Reminder set at 07:10:44 PM for 2m 30s from now
⏰ Will ping at 07:13:14 PM
💬 Message: "🐰🐰🐰"
🔊 Sound: Frog (Volume: normal)

───────────────────────── Controls ────────────────
Press Ctrl+C to cancel
──────────────────────────────────────────────────

[███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 02:18 remaining (⏰ 07:13:14 PM)
```

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