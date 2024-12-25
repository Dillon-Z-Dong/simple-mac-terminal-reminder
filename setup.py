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
    # Get home directory
    home = str(Path.home())
    
    # Default installation directory
    default_install_dir = os.path.join(home, '.local', 'bin')
    
    # Prompt for installation directory
    print(f"Enter installation directory (press Enter for default {default_install_dir}):")
    install_dir = input().strip() or default_install_dir
    
    # Create installation directory if it doesn't exist
    os.makedirs(install_dir, exist_ok=True)
    
    # Clone the repository
    repo_url = "https://github.com/Dillon-Z-Dong/simple-mac-terminal-reminder.git"
    temp_dir = os.path.join(install_dir, "simple-mac-terminal-reminder")
    
    print("\nCloning repository...")
    if not run_command(f"git clone {repo_url} {temp_dir}"):
        print("Failed to clone repository")
        return False
    
    # Copy reminder.py to installation directory
    source_file = os.path.join(temp_dir, "reminder.py")
    dest_file = os.path.join(install_dir, "reminder.py")
    
    print("Installing reminder script...")
    if not run_command(f"cp {source_file} {dest_file}"):
        print("Failed to copy reminder script")
        return False
    
    # Make the script executable
    if not run_command(f"chmod +x {dest_file}"):
        print("Failed to make script executable")
        return False
    
    # Clean up temp directory
    if not run_command(f"rm -rf {temp_dir}"):
        print("Warning: Failed to clean up temporary files")
    
    # Set up alias in .zshrc
    print("\nEnter alias name (press Enter for default 'remind'):")
    alias_name = input().strip() or "remind"
    
    zshrc_path = os.path.join(home, '.zshrc')
    alias_line = f'\n# Terminal Reminder\nexport PATH="$PATH:{install_dir}"\nalias {alias_name}="python3 {dest_file}"\n'
    
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
    
    setup_reminder()