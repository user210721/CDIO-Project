import os
from tkinter import filedialog, Tk, simpledialog

# Hide the main tkinter window
root = Tk()
root.withdraw()

# Prompt user to select multiple files
file_paths = filedialog.askopenfilenames(title="Select files to rename")

# If no files selected, exit
if not file_paths:
    print("No files selected.")
    exit()

# Prompt user for prefix text
prefix = simpledialog.askstring("Input", "Enter text to add as prefix:")

if prefix:
    for file_path in file_paths:
        folder, original_name = os.path.split(file_path)
        new_name = f"{prefix}_{original_name}"
        new_path = os.path.join(folder, new_name)
        os.rename(file_path, new_path)
        print(f"Renamed: {original_name} -> {new_name}")
    print("Renaming completed.")
else:
    print("No prefix entered. Renaming cancelled.")
