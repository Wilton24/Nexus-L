import os
import shutil

# 1. Configuration: Where is the mess?
# You can change this to your actual Downloads folder later
WATCH_DIRECTORY = "./downloads_demo"

# 2. The "Routing Table": Maps extensions to Folder Names
EXTENSION_MAP = {
    # Audio
    '.mp3': 'Audio',
    '.wav': 'Audio',
    '.flac': 'Audio',
    # Video
    '.mp4': 'Videos',
    '.mov': 'Videos',
    '.mkv': 'Videos',
    # Documents
    '.pdf': 'Documents',
    '.docx': 'Documents',
    '.txt': 'Documents',
    '.xlsx': 'Spreadsheets',
    # Images
    '.jpg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
}


def organize_folder():
    # Ensure the source directory exists so we don't crash
    if not os.path.exists(WATCH_DIRECTORY):
        print(
            f"Directory {WATCH_DIRECTORY} not found. Creating it for demo...")
        os.makedirs(WATCH_DIRECTORY)
        return

    # Loop through every file in the directory
    for filename in os.listdir(WATCH_DIRECTORY):
        file_path = os.path.join(WATCH_DIRECTORY, filename)

        # Skip if it's a folder (we only want to move files)
        if os.path.isdir(file_path):
            continue

        # Get the file extension (e.g., '.mp3')
        # os.path.splitext returns a tuple: ('filename', '.ext')
        file_ext = os.path.splitext(filename)[1].lower()

        if file_ext in EXTENSION_MAP:
            # Determine the destination folder based on our map
            category = EXTENSION_MAP[file_ext]
            target_folder = os.path.join(WATCH_DIRECTORY, category)

            # Create the category folder if it doesn't exist
            os.makedirs(target_folder, exist_ok=True)

            # Define the final destination path
            dest_path = os.path.join(target_folder, filename)

            # Logic: Move the file
            try:
                shutil.move(file_path, dest_path)
                print(f"SUCCESS: Moved {filename} to {category}/")
            except Exception as e:
                print(f"ERROR: Could not move {filename}: {e}")


if __name__ == "__main__":
    print("--- Nexus-L File Organizer Starting ---")
    organize_folder()
    print("--- Task Finished ---")
