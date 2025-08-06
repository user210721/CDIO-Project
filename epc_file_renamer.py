# EPC Batch File Renamer Tool (Folder-Recursive)
# Renames all files in a selected folder (including all subfolders) with a new base name + index (across multiple folders)

import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

last_used_index = {}  # Track last index for each base name

def select_folder():
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select Folder to Rename Files In")
    return folder_path

def get_all_files_recursive(folder_path):
    files = []
    for dirpath, _, filenames in os.walk(folder_path):
        for file in filenames:
            full_path = os.path.join(dirpath, file)
            files.append(full_path)
    return files

def show_loading_popup():
    popup = tk.Toplevel()
    popup.title("Renaming...")
    popup.geometry("300x80")
    popup.attributes("-topmost", True)
    tk.Label(popup, text="Renaming files, please wait...").pack(pady=20)
    popup.update()
    return popup

def preview_and_rename(files):
    global last_used_index

    if not files:
        print("No files found.")
        return

    sample_name = Path(files[0]).name

    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    new_base = simpledialog.askstring(
        "Rename Files",
        f"Preview: {sample_name}\n\nEnter new base name (e.g. 'Fixed Reader OR Fixed Reader_Ubi Warehouse'):"
    )

    if not new_base:
        print("❌ Rename cancelled.")
        return

    popup = show_loading_popup()

    start_index = last_used_index.get(new_base, 0) + 1

    for i, file in enumerate(files, start=start_index):
        path = Path(file)
        new_name = f"{new_base}_{i}{path.suffix}"
        new_path = path.with_name(new_name)

        try:
            os.rename(path, new_path)
            print(f"✅ Renamed: {path} → {new_path}")
        except Exception as e:
            print(f"❌ Failed to rename {path}: {e}")

    last_used_index[new_base] = start_index + len(files) - 1
    popup.destroy()

def rename_loop():
    while True:
        folder = select_folder()
        if not folder:
            print("❌ No folder selected.")
            break

        all_files = get_all_files_recursive(folder)
        preview_and_rename(all_files)

        answer = messagebox.askyesno("Another Folder?", "Do you want to rename another folder?")
        if not answer:
            break

if __name__ == "__main__":
    rename_loop()
