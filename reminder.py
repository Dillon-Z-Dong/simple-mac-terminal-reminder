#!/usr/bin/env python3
import time
import subprocess
import os

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

def create_reminder(seconds, message):
    """
    Sleep for specified seconds and then show a notification alert
    """
    print(f"Reminder set for {seconds/60:.1f} minutes from now")
    time.sleep(seconds)
    
    # Simplified AppleScript without icon
    apple_script = f'''
    tell application "System Events"
        display dialog "{message}" buttons {{"OK"}} default button "OK" with title "Reminder" with icon caution
    end tell
    '''
    
    # Run the AppleScript command
    subprocess.run(['osascript', '-e', apple_script])

def main():
    try:
        seconds, message = get_input()
        create_reminder(seconds, message)
    except KeyboardInterrupt:
        print("\nReminder cancelled")

if __name__ == "__main__":
    main()