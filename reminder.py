#!/usr/bin/env python3
import time
import subprocess
import os
import sys
from datetime import datetime, timedelta

def get_input():
    """
    Get time and message input from user
    """
    while True:
        try:
            time_input = input("Enter time (e.g., '5m' for 5 minutes, '30s' for 30 seconds): ").lower().strip()
            
            # Parse the time input
            if time_input.endswith('m'):
                minutes = float(time_input[:-1])
                seconds = minutes * 60
            elif time_input.endswith('s'):
                seconds = float(time_input[:-1])
            else:
                print("Please use 'm' for minutes or 's' for seconds (e.g., '5m' or '30s')")
                continue
                
            message = input("Enter reminder message: ").strip()
            
            if not message:
                print("Please enter a message")
                continue
                
            return seconds, message
            
        except ValueError:
            print("Please enter a valid number with 'm' or 's'")

def format_time_remaining(seconds):
    """
    Format remaining seconds into MM:SS format
    """
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes:02d}:{secs:02d}"

def draw_progress_bar(current, total, width=40):
    """
    Draw a progress bar showing elapsed time
    """
    progress = current / total
    filled = int(width * progress)
    bar = '█' * filled + '░' * (width - filled)
    time_str = format_time_remaining(total - current)
    return f'\r[{bar}] {time_str} remaining'

def create_reminder(seconds, message):
    """
    Sleep for specified seconds and then show a notification alert
    """
    start_time = time.time()
    end_time = start_time + seconds
    
    print(f"\nReminder set for {seconds/60:.1f} minutes from now")
    print("Press Ctrl+C to cancel")
    print()
    
    try:
        while time.time() < end_time:
            elapsed = time.time() - start_time
            sys.stdout.write(draw_progress_bar(elapsed, seconds))
            sys.stdout.flush()
            time.sleep(0.1)  # Update every 0.1 seconds
        
        sys.stdout.write('\n')  # New line after progress bar completes
        
    except KeyboardInterrupt:
        sys.stdout.write('\nReminder cancelled\n')
        return
    
    # Show the notification
    apple_script = f'''
    tell application "System Events"
        display dialog "{message}" buttons {{"OK"}} default button "OK" with title "Reminder" with icon caution
    end tell
    '''
    
    subprocess.run(['osascript', '-e', apple_script])

def main():
    try:
        seconds, message = get_input()
        create_reminder(seconds, message)
    except KeyboardInterrupt:
        print("\nReminder cancelled")

if __name__ == "__main__":
    main()