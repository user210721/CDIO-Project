# EPC Merger and Reconciliation Tool (Index-Based Column Selection - Batch Smart)

import pandas as pd
import os
import csv
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

all_batches = []

def select_files():
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(
        title="Select a Batch of RFID Scan Files",
        filetypes=[("Excel/CSV", "*.xlsx *.xls *.csv")]
    )
    return list(file_paths)

def choose_epc_column_gui(columns, filename, preview=None):
    root = tk.Tk()
    root.title("Select EPC Column")
    msg = f"{filename}\nSelect the column that contains EPCs:"
    if preview:
        msg += f"\n\nPreview:\n{preview}"
    tk.Label(root, text=msg).pack(padx=10, pady=10)

    var = tk.StringVar(root)
    var.set(columns[0])
    dropdown = tk.OptionMenu(root, var, *columns)
    dropdown.pack(padx=10, pady=10)

    def on_submit():
        root.quit()
        root.destroy()

    tk.Button(root, text="Confirm", command=on_submit).pack(pady=10)
    root.mainloop()

    return var.get()

def is_epc_like(value):
    if isinstance(value, str):
        value = value.strip().replace(' ', '')
        return value.isalnum() and len(value) >= 8
    return False

def read_file_flexible(file, nrows=None):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            sample = f.read(2048)
            dialect = csv.Sniffer().sniff(sample)
        df = pd.read_csv(file, delimiter=dialect.delimiter, skiprows=3, nrows=nrows)
        if df.columns.str.contains("//").any():
            df = pd.read_csv(file, delimiter=dialect.delimiter, header=None, nrows=nrows)
    except Exception:
        try:
            df = pd.read_csv(file, delimiter=',', skiprows=3, on_bad_lines='skip', nrows=nrows)
        except Exception:
            df = pd.read_csv(file, delimiter=',', header=None, on_bad_lines='skip', nrows=nrows)

    for i, row in df.iterrows():
        if row.astype(str).str.upper().str.contains("TAG").any():
            df.columns = df.iloc[i].values
            df = df.iloc[i+1:].reset_index(drop=True)
            break
    return df

def load_batch(files):
    preview_df = read_file_flexible(files[0], nrows=10)
    preview_df = preview_df.dropna(axis=1, how='all').dropna(axis=0, how='all')
    preview_rows = preview_df.head(3).astype(str).agg(', '.join, axis=1).tolist()
    preview_text = "\n".join(preview_rows)

    columns_list = preview_df.columns.tolist()
    epc_col = choose_epc_column_gui([str(col) for col in columns_list], Path(files[0]).name, preview_text)
    epc_index = columns_list.index(epc_col)

    batch_epcs = []
    for file in files:
        print(f"Reading file: {file}")
        df = read_file_flexible(file)
        df = df.dropna(axis=1, how='all').dropna(axis=0, how='all')

        if epc_index >= len(df.columns):
            print(f"❌ Skipping {file} — column index {epc_index} out of range.")
            continue

        selected_col = df.columns[epc_index]
        df = df[[selected_col]].dropna()
        df.columns = ["EPC"]
        df = df[df["EPC"].apply(is_epc_like)]
        df["Detected Location"] = Path(file).stem
        batch_epcs.append(df)

    if batch_epcs:
        merged_batch = pd.concat(batch_epcs, ignore_index=True)
        all_batches.append(merged_batch)
        print(f"✅ Batch of {len(files)} files added.")
    else:
        print("⚠️ No valid EPC data found in this batch.")

if __name__ == "__main__":
    print("Starting EPC Merger Tool (Batch Mode)...")
    while True:
        selected_files = select_files()
        if not selected_files:
            break
        load_batch(selected_files)
        add_more = messagebox.askyesno("Add Another Batch?", "Do you want to load another batch of files?")
        if not add_more:
            break

    if all_batches:
        confirm_merge = messagebox.askyesno("Confirm Merge", "Are you sure you want to merge all uploaded batches and save?")
        if confirm_merge:
            final_merged = pd.concat(all_batches, ignore_index=True)
            final_merged = final_merged.drop_duplicates(subset="EPC").sort_values("EPC")
            final_merged.to_excel("Merged_Cleaned_EPCs.xlsx", index=False)
            print("✅ All batches merged and saved to 'Merged_Cleaned_EPCs.xlsx'")
        else:
            print("❌ Merge cancelled. No file was saved.")
    else:
        print("❌ No EPC data was merged.")
