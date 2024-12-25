#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path

def run_command(command):
    """Run a shell command and handle errors"""
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error details: {e}")
        return False

def setup_reminder():
    """Setup the reminder tool"""
    print("Starting terminal reminder setup...")
    
    # Get home directory
    home = str(Path.home())
    print(f"Home directory identified as: {home}")
    
    # Default installation directory
    default_install_dir = os.path.join(home, '.local', 'bin')
    
    # Prompt for installation directory
    print(f"\nEnter installation directory (press Enter for default {default_install_dir}):")
    install_dir = input().strip() or default_install_dir
    print(f"Using installation directory: {install_dir}")
    
    # Create installation directory if it doesn't exist
    if not os.path.exists(install_dir):
        print(f"Creating installation directory: {install_dir}")
        os.makedirs(install_dir, exist_ok=True)
    else:
        print(f"Installation directory already exists: {install_dir}")
    
    # Set up alias in .zshrc
    print("\nEnter alias name (press Enter for default 'remind'):")
    alias_name = input().strip() or "remind"
    print(f"Using alias name: {alias_name}")
    
    # Validate that reminder.py exists in current directory
    if not os.path.exists("reminder.py"):
        print("Error: reminder.py not found in current directory")
        print("Please make sure you're in the repository directory")
        return False
    
    # Copy reminder.py to installation directory
    dest_file = os.path.join(install_dir, "reminder.py")
    print(f"\nCopying reminder.py to: {dest_file}")
    if not run_command(f"cp reminder.py {dest_file}"):
        print("Failed to copy reminder script")
        return False
    
    # Make the script executable
    print("Making script executable...")
    if not run_command(f"chmod +x {dest_file}"):
        print("Failed to make script executable")
        return False
    
    # Update .zshrc
    zshrc_path = os.path.join(home, '.zshrc')
    alias_line = f'\n# Terminal Reminder\nexport PATH="$PATH:{install_dir}"\nalias {alias_name}="python3 {dest_file}"\n'
    
    print(f"\nUpdating {zshrc_path} with:")
    print(f"- Adding {install_dir} to PATH")
    print(f"- Creating alias: {alias_name}")
    
    try:
        with open(zshrc_path, 'a') as f:
            f.write(alias_line)
    except Exception as e:
        print(f"Error updating .zshrc: {e}")
        return False
    
    print("\nInstallation complete!")
    print(f"Script installed in: {install_dir}")
    print(f"Alias '{alias_name}' created")
    print("\nPlease run 'source ~/.zshrc' or restart your terminal to use the tool")
    return True

if __name__ == "__main__":
    if sys.platform != "darwin":
        print("This script is only supported on macOS")
        sys.exit(1)
    
    setup_reminder() d