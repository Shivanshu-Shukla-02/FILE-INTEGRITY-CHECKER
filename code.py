import os
import hashlib
import json
import time

# Configuration
HASH_FILE = "file_hashes.json"
CHECK_INTERVAL = 10  # Time in seconds between checks

# Function to calculate the SHA-256 hash of a file
def calculate_hash(file_path):
    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    except (OSError, IOError):
        return None

# Function to load stored hash data
def load_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            return json.load(f)
    return {}

# Function to save hash data
def save_hashes(hashes):
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=4)

# Function to monitor changes in the directory
def monitor_directory(directory):
    previous_hashes = load_hashes()
    current_hashes = {}

    # Traverse directory and calculate hashes
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)
            if file_hash:
                current_hashes[file_path] = file_hash

    # Compare hashes and detect changes
    added_files = set(current_hashes.keys()) - set(previous_hashes.keys())
    deleted_files = set(previous_hashes.keys()) - set(current_hashes.keys())
    modified_files = {
        file for file in current_hashes.keys() & previous_hashes.keys()
        if current_hashes[file] != previous_hashes[file]
    }

    # Print changes
    if added_files:
        print("Added files:")
        for file in added_files:
            print(f"  {file}")

    if deleted_files:
        print("Deleted files:")
        for file in deleted_files:
            print(f"  {file}")

    if modified_files:
        print("Modified files:")
        for file in modified_files:
            print(f"  {file}")

    # Save the current state
    save_hashes(current_hashes)

# Main function
def main():
    directory = input("Enter the directory to monitor: ").strip()
    if not os.path.isdir(directory):
        print("Invalid directory. Please provide a valid path.")
        return

    print(f"Monitoring changes in: {directory}")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            monitor_directory(directory)
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    main()
