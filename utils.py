import os
import sys
import platform
import subprocess

def choose_team():
    while True:
        print("\nChoose your team:")
        print("[1] Red Team (Attacker)")
        print("[2] Blue Team (Defender)")
        choice = input("Enter your choice (1/2): ").strip()
        if choice in ['1', '2']:
            return "Red" if choice == "1" else "Blue"
        print("\nInvalid choice. Please enter 1 or 2.")

def execute_command(command, base_dir=None):
    if not command or not command.strip():
        return ""
        
    cmd_clean = command.strip()
    
    # Handle exit/quit
    if cmd_clean.lower() in ['exit', 'quit']:
        print("\nExiting CyberArena Security. Goodbye!")
        sys.exit(0)
        
    try:
        # Handle cd variations
        if cmd_clean.lower() == 'cd':
            return f"Current directory: {os.getcwd()}"
            
        if cmd_clean.lower().startswith(('cd ', 'cd..', 'cd\\', 'cd/')):
            if cmd_clean.lower() == 'cd..':
                new_dir = '..'
            elif cmd_clean.lower().startswith('cd '):
                new_dir = cmd_clean[3:].strip()
            else:
                new_dir = cmd_clean[2:].strip()

            target_path = os.path.abspath(new_dir if new_dir else '.')
            
            # Sandbox protection: keep user within challenge directory if base_dir is set
            if base_dir:
                base_abs = os.path.abspath(base_dir)
                if not target_path.startswith(base_abs):
                    return f"Access restricted: cannot navigate outside challenge environment ({base_abs})"
                    
            os.chdir(target_path)
            return f"Changed directory to {os.getcwd()}"
        else:
            result = subprocess.run(command, shell=True, text=True, capture_output=True, errors='replace')
            output = result.stdout if result.stdout else result.stderr
            return output if output else "Command executed with no output."
    except Exception as e:
        return f"Error executing command: {str(e)}"

def get_os_type():
    return "Windows" if platform.system() == "Windows" else "Linux"