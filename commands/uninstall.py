import os

def run(args):
    if not args:
        print("Usage: uninstall <command1> [<command2> ...]")
        return

    for command in args:
        filename = f"commands/{command}.py"
        
        if os.path.exists(filename):
            confirm = input(f"Are you sure you want to uninstall '{command}'? (y/N): ").strip().lower()
            if confirm == 'y':
                os.remove(filename)
                print(f"Uninstalled '{command}'.")
            else:
                print(f"Skipped '{command}'.")
        else:
            print(f"Command '{command}' not found.")
