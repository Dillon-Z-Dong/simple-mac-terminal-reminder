#!/usr/bin/env python3
import time
import subprocess
import os
import sys
import re
from datetime import datetime, timedelta

def set_terminal_title(title):
    """
    Set the terminal window title using ANSI escape codes
    """
    sys.stdout.write(f"\x1b]0;{title}\x07")
    sys.stdout.flush()

def restore_terminal_title():
    """
    Restore the terminal window title to default
    """
    sys.stdout.write("\x1b]0;\x07")
    sys.stdout.flush()

def parse_time(time_input):
    """
    Parse time input in various formats:
    - Plain number (assumed minutes)
    - Format like '5m30s'
    - Format like '5m' or '30s'
    """
    time_input = str(time_input).lower().strip()
    
    # Check for format like '5m30s'
    combined_pattern = re.match(r'^(\d+)m(\d+)s$', time_input)
    if combined_pattern:
        minutes = int(combined_pattern.group(1))
        seconds = int(combined_pattern.group(2))
        return minutes * 60 + seconds
        
    # Check for single unit format
    if time_input.endswith('m'):
        return float(time_input[:-1]) * 60
    elif time_input.endswith('s'):
        return float(time_input[:-1])
    
    # Assume minutes if no unit specified
    try:
        return float(time_input) * 60
    except ValueError:
        raise ValueError("Invalid time format")

def get_input():
    """
    Get time and message input from user or command line
    """
    # Check command line arguments
    if len(sys.argv) > 1:
        try:
            seconds = parse_time(sys.argv[1])
            message = sys.argv[2] if len(sys.argv) > 2 else input("Enter reminder message: ").strip()
            
            if not message:
                print("Please enter a message")
                return get_input()
                
            return seconds, message
            
        except (ValueError, IndexError):
            print("Invalid command line input, falling back to interactive mode")
    
    # Interactive input mode
    while True:
        try:
            time_input = input("Enter time (e.g., '5' for 5 minutes, '5m30s', '30s'): ")
            seconds = parse_time(time_input)
            
            message = input("Enter reminder message: ").strip()
            
            if not message:
                print("Please enter a message")
                continue
                
            return seconds, message
            
        except ValueError:
            print("Please enter a valid time (e.g., '5' for 5 minutes, '5m30s', '30s')")

def format_time_remaining(seconds):
    """
    Format remaining seconds into MM:SS format
    """
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes:02d}:{secs:02d}"

def draw_progress_bar(current, total, end_time, width=40):
    """
    Draw a progress bar showing elapsed time
    """
    progress = current / total
    filled = int(width * progress)
    bar = '█' * filled + '░' * (width - filled)
    time_str = format_time_remaining(total - current)
    return f'\r[{bar}] {time_str} remaining (⏰ {end_time.strftime("%I:%M:%S %p")})'

def create_reminder(seconds, message):
    """
    Sleep for specified seconds and then show a notification alert
    """
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=seconds)
    
    # Set terminal title
    set_terminal_title(f"Reminder for {end_time.strftime('%I:%M %p')}: {message}")
    
    # Clear some space between input and display
    print("\n" + "─" * 50)
    
    # Display reminder information
    print(f"\n🕰️  Reminder set at {start_time.strftime('%I:%M:%S %p')} for {seconds/60:.1f} minutes from now")
    print(f"⏰ Will ping at {end_time.strftime('%I:%M:%S %p')}")
    print(f"💬 Message: \"{message}\"")
    print("\n" + "─" * 25 + " Controls " + "─" * 16)
    print("Press Ctrl+C to cancel")
    print("─" * 50 + "\n")
    
    try:
        while datetime.now() < end_time:
            elapsed = (datetime.now() - start_time).total_seconds()
            sys.stdout.write(draw_progress_bar(elapsed, seconds, end_time))
            sys.stdout.flush()
            time.sleep(0.1)  # Update every 0.1 seconds
        
        sys.stdout.write('\n')  # New line after progress bar completes
        
    except KeyboardInterrupt:
        sys.stdout.write('\nReminder cancelled\n')
        restore_terminal_title()
        return
    
    # Show the notification
    apple_script = f'''
    tell application "System Events"
        display dialog "{message}" buttons {{"OK"}} default button "OK" with title "Reminder" with icon caution
    end tell
    '''
    
    subprocess.run(['osascript', '-e', apple_script])
    restore_terminal_title()

def main():
    try:
        seconds, message = get_input()
        create_reminder(seconds, message)
    except KeyboardInterrupt:
        print("\nReminder cancelled")
        restore_terminal_title()

if __name__ == "__main__":
    main()