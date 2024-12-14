#!/usr/bin/env python3
import time
import subprocess
import os
import sys
import re
import argparse
import random
import threading
from datetime import datetime, timedelta

# Sound configuration
SOUND_VOLUMES = {
    'loud': 7,      # High volume, near maximum (0-14 scale in AppleScript)
    'normal': 5,    # Medium volume
    'quiet': 2,     # Low volume
    'none': 0       # Muted
}

AVAILABLE_SOUNDS = [
    'Blow', 'Bottle', 'Frog', 'Funk', 'Glass', 'Hero',
    'Morse', 'Ping', 'Pop', 'Purr', 'Sosumi', 'Submarine', 'Tink'
]

def set_terminal_title(title):
    """Set the terminal window title using ANSI escape codes"""
    sys.stdout.write(f"\x1b]0;{title}\x07")
    sys.stdout.flush()

def restore_terminal_title():
    """Restore the terminal window title to default"""
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


def get_input_with_default(prompt, default, help_type=None):
    """Get user input with a default value and help option"""
    suffix = f" (default ➜ {default})"
    while True:
        response = input(f"{prompt}{suffix}: ").strip()
        if response == '?' and help_type:
            show_help(help_type)
            continue
        return response if response else default

def get_random_sound():
    """Return a random sound from available options"""
    return random.choice(AVAILABLE_SOUNDS)

def get_input(args=None):
    """Get time and message input from user or command line"""
    if args:
        return (
            parse_time(args.time),
            args.message,
            args.volume,
            args.sound if args.sound != 'random' else get_random_sound()
        )
    
    # Interactive input mode
    print("─" * 50)
    print("📋 Reminder Setup (Enter ➜ default, ? ➜ help)")
    print("─" * 50)
    
    # Get time input
    time_input = get_input_with_default("Time", "5m0s", "time").strip()
    seconds = parse_time(time_input)
    
    # Generate default message based on time
    minutes = int(seconds // 60)
    remaining_seconds = int(seconds % 60)
    if minutes > 0 and remaining_seconds > 0:
        default_msg = f"{minutes}m {remaining_seconds}s reminder"
    elif minutes > 0:
        default_msg = f"{minutes} minute reminder"
    else:
        default_msg = f"{remaining_seconds} second reminder"
    
    print("─" * 50)
    # Get message with help option
    message = get_input_with_default("Message", default_msg, "message")
    
    print("─" * 50)
    # Get sound first, then volume
    sound = get_input_with_default("Sound", "random", "sound").lower()
    if sound == "random":
        sound = get_random_sound()
    elif sound not in [s.lower() for s in AVAILABLE_SOUNDS]:
        print(f"Invalid sound. Using random sound: {get_random_sound()}")
        sound = get_random_sound()
    else:
        # Find the correct case from AVAILABLE_SOUNDS
        sound = next(s for s in AVAILABLE_SOUNDS if s.lower() == sound.lower())
    
    print("─" * 50)
    volume = get_input_with_default("Volume", "normal", "volume").lower()
    if volume not in SOUND_VOLUMES:
        print("Invalid volume level. Using normal")
        volume = 'normal'
    
    print("─" * 50)    
    return seconds, message, volume, sound

def show_help(prompt_type):
    """Show detailed help for different input types"""
    help_text = {
        'time': """
Time can be specified in several formats:
- Minutes: 5 (same as 5m)
- Minutes and seconds: 5m30s
- Seconds only: 30s
        """,
        'sound': f"""
Available sounds: {', '.join(AVAILABLE_SOUNDS)}
Enter 'random' to let the system choose one for you.
        """,
        'volume': """
Volume levels:
- loud: Maximum volume
- normal: Medium volume
- quiet: Low volume
- none: Muted
        """,
        'message': """
Enter any text you'd like to see when the reminder pops up.
        """
    }
    print(help_text.get(prompt_type, "No help available for this option"))

def format_time_remaining(seconds):
    """Format remaining seconds into MM:SS format"""
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes:02d}:{secs:02d}"

def draw_progress_bar(current, total, end_time, width=40):
    """Draw a progress bar showing elapsed time"""
    progress = current / total
    filled = int(width * progress)
    bar = '█' * filled + '░' * (width - filled)
    time_str = format_time_remaining(total - current)
    return f'\r[{bar}] {time_str} remaining (⏰ {end_time.strftime("%I:%M:%S %p")})'

def create_reminder(seconds, message, volume='normal', sound='Purr', snooze_count=0):
    """Sleep for specified seconds and then show a notification alert"""
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=seconds)
    
    # Set terminal title
    set_terminal_title(f"Reminder for {end_time.strftime('%I:%M %p')}: {message}")
    
    # Display reminder information
    print("\n" + "─" * 50)
    print(f"\n🕰️  Reminder set at {start_time.strftime('%I:%M:%S %p')} for {int(seconds//60)}m {int(seconds%60):02d}s from now")
    print(f"⏰ Will ping at {end_time.strftime('%I:%M:%S %p')}")
    print(f"💬 Message: \"{message}\"")
    print(f"🔊 Sound: {sound} (Volume: {volume})")
    if snooze_count > 0:
        print(f"💤 Snooze count: {snooze_count}")
    print("\n" + "─" * 25 + " Controls " + "─" * 16)
    print("Press Ctrl+C to cancel")
    print("─" * 50 + "\n")
    
    try:
        while datetime.now() < end_time:
            elapsed = (datetime.now() - start_time).total_seconds()
            sys.stdout.write(draw_progress_bar(elapsed, seconds, end_time))
            sys.stdout.flush()
            time.sleep(0.1)
        
        sys.stdout.write('\n')
        
    except KeyboardInterrupt:
        sys.stdout.write('\nReminder cancelled\n')
        restore_terminal_title()
        return
    
    current_time = datetime.now().strftime("%I:%M %p")
    duration_str = f"{int(seconds//60)}m {int(seconds%60):02d}s"
    
    def play_sound_thread():
        """Play the notification sound in a separate thread"""
        if volume != 'none':
            sound_script = f'''
            tell application "System Events"
                set originalVolume to output volume of (get volume settings)
                set volume output volume {SOUND_VOLUMES[volume] * 14}
                do shell script "afplay /System/Library/Sounds/{sound}.aiff"
                set volume output volume originalVolume
            end tell
            '''
            subprocess.run(['osascript', '-e', sound_script])
    
    # Start sound in background thread
    if volume != 'none':
        sound_thread = threading.Thread(target=play_sound_thread)
        sound_thread.start()
    
    # Show the rich notification dialog
    if snooze_count == 0:
        snooze_info = ""
    elif snooze_count == 1:
        snooze_info = f"\\n💤 Snoozed 1 time"
    else:
        snooze_info = f"\\n💤 Snoozed {snooze_count} times"
        
    apple_script_rich = f'''
    tell application "System Events"
        set theAlertText to "⌛️ {duration_str}\\n🕐 Current time: {current_time}{snooze_info}\\n\\n{message}"
        display dialog theAlertText ¬
            with title "🕰️ Reminder!" ¬
            buttons {{"Got it", "+5 min"}} ¬
            default button "Got it" ¬
            with icon note
        set button_pressed to button returned of result
        return button_pressed
    end tell
    
    # Show the notification as well
    display notification "{message}" with title "🕰️ Reminder!" subtitle "{duration_str} • {current_time}"
    '''
    
    result = subprocess.run(['osascript', '-e', apple_script_rich], capture_output=True, text=True)
    restore_terminal_title()
    
    # Wait for sound to finish if it's playing
    if volume != 'none':
        sound_thread.join()
    
    # If +5 min was clicked, create a new reminder
    if result.stdout.strip() == "+5 min":
        create_reminder(300, message, volume, sound, snooze_count + 1)

def main():
    parser = argparse.ArgumentParser(description='Set a reminder with custom sound options')
    parser.add_argument('time', nargs='?', help='Time duration (e.g., 5, 5m, 5m30s)')
    parser.add_argument('message', nargs='?', help='Reminder message')
    parser.add_argument('-v', '--volume', choices=['loud', 'normal', 'quiet', 'none'],
                      default='normal', help='Sound volume level')
    parser.add_argument('-s', '--sound', choices=AVAILABLE_SOUNDS + ['random'],
                      default='random', help='Sound effect')
    
    args = parser.parse_args()
    
    try:
        if args.time and args.message:
            seconds, message, volume, sound = get_input(args)
        else:
            seconds, message, volume, sound = get_input()
        
        create_reminder(seconds, message, volume, sound)
    except KeyboardInterrupt:
        print("\nReminder cancelled")
        restore_terminal_title()

if __name__ == "__main__":
    main()