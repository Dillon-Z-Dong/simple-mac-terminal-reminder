# simple-mac-terminal-reminder
A simple python script that prompts you for a time and message. After that time, the message will appear as a system notification pop up (which will appear over other windows). Can be cancelled with Ctrl+C before the reminder triggers. 

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

Once installed, you can create reminders from your terminal:

1. Type `remind` in your terminal
2. Enter the time duration when prompted:
   - Use `m` for minutes (e.g., `5m` for 5 minutes)
   - Use `s` for seconds (e.g., `30s` for 30 seconds)
3. Enter your reminder message when prompted
4. A pop-up notification will appear after the specified time

Example:
```bash
$ remind
Enter time (e.g., '5m' for 5 minutes, '30s' for 30 seconds): 15m
Enter reminder message: Check the oven
Reminder set for 15.0 minutes from now
```
