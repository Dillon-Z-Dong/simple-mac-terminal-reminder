# simple-mac-terminal-reminder

A simple command line tool for MacOS for reminding yourself of things in the near future. Just open up your default Terminal app, type a command like 

```bash
$ remind 15m "Get pizza from oven" 
```

and never worry about burnt pizza again!

## What a reminder looks like:

Once you set a reminder, a progress bar will appear in the tab where you ran the command. Feel free to tab away; you can check back on the bar at any time. You can also Ctrl+C to cancel the reminder.

```
──────────────────────────────────────────────────────
🕰️  Reminder set at 6:30:15 PM for 15m 00s from now
⏰ Will ping at 6:45:15 PM
💬 Message: "Get pizza from oven!"
🔊 Sound: Purr (Volume: loud)
─────────────── Controls ────────────────
Press Ctrl+C to cancel
──────────────────────────────────────────────────────

[██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 09:15 remaining (⏰ 6:45:15 PM)
```

Once the time is up, a sound will play and you'll get a popup (that appears above all other apps) with options to dismiss the reminder ("Got it") or snooze it (+5 min). Snoozing will launch another ```reminder``` instance in the same tab, and you can decide again in 5 min.

```
╔══════════════ 🕰️ Reminder! ══════════════╗
║ ⌛️ 15m00s                                ║
║ 🕐 Current time: 10:45 AM                ║
║ 💤 Snoozed 1 time                        ║
║                                          ║
║ Respond to email!                        ║
║                                          ║
║             [Got it] [+5 min]            ║
╚══════════════════════════════════════════╝
```

## How to set a reminder:

#### 1. Command line arguments

The quickest and easiest way to set a reminder is with command line arguments (run from the default MacOS Terminal app)

Set a 1 minute timer with a default message ("1 minute reminder"):
```bash
$ remind 1
```

Set a 3 minute 30 second timer with a custom message ("Green tea done steeping"):
```bash
$ remind 3m30s "Green tea done steeping"
```

Set a 25 minute timer with a custom message ("Pomodoro 🍅"), sound ("Funk"), and volume ("quiet")
```bash
$ remind 25m "Pomodoro 🍅" -s Funk -v quiet 
```

#### 2. Interactive prompt

You can also see all of the available options in interactive mode. To launch this, just type "remind" with no other arguments. Type `?` at any prompt for help.

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


## Installation

Installation is easy. Just clone the repository to your desired installation location and run the setup script.

### Requirements

- macOS 
- Git (required only for installation)

### Installation Steps

1. Clone the repository to your desired installation location (e.g. your home directory):
```bash
cd ~ # Change this to any installation directory you want
git clone https://github.com/Dillon-Z-Dong/simple-mac-terminal-reminder.git
cd simple-mac-terminal-reminder
```

2. Run the setup script:
```bash
python3 setup.py
```
The setup script will:
- Make the reminder script executable
- Ask for your preferred alias name (defaults to 'remind')
- Add the installation directory to your PATH
- Create the alias in your .zshrc

3. Source your .zshrc or restart your terminal:
```bash
source ~/.zshrc
```

4. Try running the alias you set!

