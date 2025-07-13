import json
import os
import time
import sys
import random
import itertools

# Colors
PURPLE = "\033[95m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Banner with typewriter effect
def typewriter(text, delay=0.003):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner_art = PURPLE + r'''
     ___  ________  ________  ________   ________ ___  ___  ________  ___  ________  ________      
    |\  \|\   ____\|\   __  \|\   ___  \|\  _____\\  \|\  \|\   ____\|\  \|\   __  \|\   ___  \    
    \ \  \ \  \___|\ \  \|\  \ \  \\ \  \\ \  \__/\ \  \\\  \ \  \___|\ \  \ \  \|\  \\ \  \\ \  \   
 __ \ \  \ \_____  \ \  \\\  \ \  \\ \  \\ \   __\\ \  \\\  \ \_____  \ \  \ \  \\\  \\ \  \\ \  \  
|\  \\_\  \|____|\  \ \  \\\  \ \  \\ \  \\ \  \_| \ \  \\\  \|____|\  \ \  \ \  \\\  \\ \  \\ \  \ 
\ \________\____\_\  \ \_______\ \__\\ \__\\ \__\   \ \_______\____\_\  \ \__\ \_______\\__\\ \__\
 \|________|\_________\|_______|\|__| \|__|\|__|    \|_______|\_________\|__|\|_______|\|__| \|__|
           \|_________|                                      \|_________|                         
    ''' + RESET
    typewriter(banner_art, 0.0005)
    typewriter(PURPLE + "💜 Version 1.1 | Created by Aashish_Cyber_H4CKS" + RESET)
    print()

# Animated loader
def animated_loader(task="Loading"):
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    for _ in range(20):
        sys.stdout.write(f"\r{CYAN}[⏳] {task}... " + next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
    print(RESET + "\n")

# Accurate progress bar
def progress_bar(current, total):
    percent = int((current / total) * 100)
    bar = "█" * (percent // 10) + "▒" * (10 - percent // 10)
    sys.stdout.write(f"\r📊 Merging: {bar} {percent}% ")
    sys.stdout.flush()

# Merging logic with save-as feature
def merge_json_files(paths):
    merged_data = []
    total_files = len(paths)

    for i, path in enumerate(paths, start=1):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    merged_data.extend(data)
                else:
                    print(RED + f"[!] Skipping non-list JSON: {path}" + RESET)
        except Exception as e:
            print(RED + f"[!] Error reading {path}: {e}" + RESET)

        progress_bar(i, total_files)
        time.sleep(0.1)

    output_path = input("\n\n💾 Enter the filename to save merged JSON (e.g., netflix.json): ").strip()
    if not output_path.endswith(".json"):
        output_path += ".json"

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, indent=4)

    print(GREEN + f"\n🎉 Successfully merged files into: {output_path}" + RESET)

# Scan folder for .json files
def get_files_from_folder(folder_path):
    json_files = []
    for file in os.listdir(folder_path):
        if file.endswith('.json'):
            full_path = os.path.join(folder_path, file)
            if os.path.isfile(full_path):
                json_files.append(full_path)
    return json_files

if __name__ == "__main__":
    banner()
    file_paths = []

    while True:
        print(CYAN + """
1️⃣  Manually add JSON file paths and merge
2️⃣  Merge all JSON files from a folder
3️⃣  Exit the tool
""" + RESET)

        choice = input("Select an option (1/2/3): ").strip()

        if choice == '1':
            try:
                num = int(input("Enter the number of files you want to merge: "))
            except ValueError:
                print(RED + "[!] Invalid input. Please enter a number." + RESET)
                continue

            for i in range(num):
                path = input(f"Enter the path for file {i+1}: ")
                if os.path.exists(path):
                    file_paths.append(path)
                else:
                    print(RED + "[!] File not found. Skipping..." + RESET)

            while True:
                extra = input("Do you want to add one more JSON file? (y/n): ").lower()
                if extra == 'y':
                    path = input("Enter the path: ")
                    if os.path.exists(path):
                        file_paths.append(path)
                    else:
                        print(RED + "[!] File not found. Skipping..." + RESET)
                elif extra == 'n':
                    break
                else:
                    print(RED + "[!] Invalid option. Please enter 'y' or 'n'." + RESET)

        elif choice == '2':
            folder_path = input("Enter the folder path: ")
            if os.path.isdir(folder_path):
                file_paths = get_files_from_folder(folder_path)
                print(f"\n📁 Found {len(file_paths)} JSON files in the folder.")
            else:
                print(RED + "[!] Folder not found. Try again." + RESET)
                continue

        elif choice == '3':
            typewriter(GREEN + "\n👋 Thanks for using JsonFusion. See you soon!" + RESET)
            break

        else:
            print(RED + "[!] Invalid choice. Try again." + RESET)
            continue

        if not file_paths:
            print(RED + "[!] No valid files to merge. Returning to menu..." + RESET)
            continue

        print("\n⏳ Preparing to merge files...")
        animated_loader("Validating & Merging")
        merge_json_files(file_paths)
        file_paths.clear()
