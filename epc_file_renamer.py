# EPC Batch File Renamer Tool
# Lets user select multiple files, preview one, and apply a unified filename pattern

import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def select_files():
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(title="Select files to rename")
    return list(file_paths)

def preview_and_rename(files):
    if not files:
        print("No files selected.")
        return

    # Preview first file name
    sample_name = Path(files[0]).name

    root = tk.Tk()
    root.withdraw()
    new_base = simpledialog.askstring("Rename Files", f"Preview: {sample_name}\n\nEnter new base name (e.g. 'Fixed Reader_Ubi Warehouse'):")

    if not new_base:
        print("❌ Rename cancelled.")
        return

    # Rename all files with new base + index
    for i, file in enumerate(files, start=1):
        path = Path(file)
        new_name = f"{new_base}_{i}{path.suffix}"
        new_path = path.with_name(new_name)
        os.rename(path, new_path)
        print(f"✅ Renamed: {path.name} → {new_name}")

if __name__ == "__main__":
    selected_files = select_files()
    preview_and_rename(selected_files)
