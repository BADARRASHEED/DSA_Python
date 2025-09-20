"""
This script clears everything (files + folders) from the Downloads folder.

⚠️ WARNING:
- All items will be permanently deleted (they do NOT go to Recycle Bin/Trash).
- Be careful before running.
"""

import os, shutil

# Step 1: Change directory to Downloads
os.chdir("../../Downloads")  # Adjust path as needed
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# Step 2: Loop through all items in Downloads
for item in os.listdir(cwd):
    path = os.path.join(cwd, item)  # Full path to the item
    
    # Step 3: Delete files
    if os.path.isfile(path):
        os.remove(path)
        print(f"Deleted file: {item}")
    
    # Step 4: Delete folders (with their contents)
    elif os.path.isdir(path):
        shutil.rmtree(path)
        print(f"Deleted folder: {item}")

# Step 5: Show what remains
print("Remaining items:", os.listdir(cwd))
