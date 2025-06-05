# EPC File Format Sorter by Header Structure
# Groups CSV files in a selected folder into subfolders (FormatGroup_X) based on column count + header signature

import os
import pandas as pd
from pathlib import Path
from collections import defaultdict
import tkinter as tk
from tkinter import filedialog

def get_format_signature(file_path):
    try:
        if file_path.suffix.lower() == '.csv':
            df = pd.read_csv(file_path, nrows=5, header=None)
        elif file_path.suffix.lower() in ['.xlsx', '.xls']:
            df = pd.read_excel(file_path, nrows=5, header=None)
        else:
            return "Unsupported"

        # Remove fully empty rows and columns
        df = df.dropna(axis=0, how='all').dropna(axis=1, how='all')

        # Delete if file is truly empty
        if df.empty or file_path.stat().st_size == 0:
            print(f"🗑️ Deleting empty file: {file_path.name}")
            file_path.unlink()
            return "Deleted"

        col_count = len(df.columns)

        # Check full RFID structure
        first_row = df.iloc[0].astype(str).str.lower()
        is_full_format = (
            col_count >= 5 and
            any("epc" in cell for cell in first_row) and
            any("rssi" in cell for cell in first_row)
        )

        # Check raw EPC-only
        sample_values = df.iloc[:, 0].astype(str)
        is_raw_epc = col_count <= 2 and sample_values.str.match(r"^[0-9A-Fa-f]{8,}$").mean() > 0.7

        if is_full_format:
            return "Format_RFID"
        elif is_raw_epc:
            return "Format_Raw_EPC"
        else:
            return "Format_Unknown"

    except Exception as e:
        print(f"❌ Could not read {file_path.name}: {e}")
        return "Unreadable"






def group_and_sort_files():
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title="Select Folder Containing EPC CSV Files")
    if not folder:
        print("❌ No folder selected.")
        return

    folder_path = Path(folder)
    grouped = defaultdict(list)

    for file in folder_path.glob("*.csv"):
        signature = get_format_signature(file)
        grouped[signature].append(file)

    # Sort into FormatGroup_X folders
    for idx, (signature, files) in enumerate(grouped.items(), start=1):
        group_folder = folder_path / f"FormatGroup_{idx}"
        group_folder.mkdir(exist_ok=True)

        for f in files:
            dest = group_folder / f.name
            f.rename(dest)

        print(f"✅ Moved {len(files)} files to {group_folder.name} ({signature})")

if __name__ == "__main__":
    group_and_sort_files()
