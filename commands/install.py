# commands/install.py

import os
import urllib.request

def run(args):
    if not args:
        print("Usage: install <command1> [<command2> ...]")
        return

    os.makedirs("commands", exist_ok=True)
    repo_base_url = "https://raw.githubusercontent.com/Bean-Pringles/Spoke-Commands/main/commands/"

    for command_name in args:
        filename = f"{command_name}.py"
        download_url = repo_base_url + filename
        dest_path = os.path.join("commands", filename)

        # Check if file exists
        if os.path.exists(dest_path):
            confirm = input(f"'{filename}' already exists. Overwrite? (y/N): ").strip().lower()
            if confirm != 'y':
                print(f"Skipped '{command_name}'")
                continue

        try:
            print(f"Installing '{command_name}' from {download_url}...")
            urllib.request.urlretrieve(download_url, dest_path)
            print(f"Installed '{command_name}' to commands/{filename}")
        except Exception as e:
            print(f"Failed to install '{command_name}': {e}")
