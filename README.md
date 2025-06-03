# EPC Merger Tool (v1.2)

A Python-based tool for merging RFID scan files and reconciling EPCs across different locations and readers. Designed for stocktaking workflows, especially where large batches of scanned files are handled.

## 🔧 Features

### 🧠 Intelligent Batch Merging
- Select multiple CSV/Excel files per batch
- Select EPC column once; applies to all files in batch by column index
- Handles inconsistent column headers automatically

### ⚡ Fast & Robust
- Skips broken/empty files gracefully
- No more `csv.Sniffer()` delays
- Reads only first few rows for preview, not whole file

### 🏷️ Metadata Extraction
- Extracts `Reader`, `Location`, and `File Name` from filenames (e.g. `Fixed Reader_Gul Drive_1.csv`)
- Adds them as columns to merged data

### 💾 Clean Output
- Outputs saved to `merged/` folder
- Prompts user to name each merged file
- Prevents overwrites with timestamped default filenames

### 🔁 Final Merger Tool
- A separate script for combining previously merged files
- Retains all metadata columns (`Reader`, `Location`, etc.)
- Output saved in `merged_final/`

## 📁 File Structure
```
/epc_merger_tool
├── epc_merger.py              # Main merging tool (raw scan merging)
├── epc_merged_file_merger.py # Final merger for cleaned files
├── merged/                    # Intermediate merged batches
├── merged_final/             # Final consolidated output
└── README.md                 # This file
```

## 🛠 Requirements
- Python 3.10+
- pandas
- tkinter (standard in most Python installs)

## 🚀 How to Run
```bash
python epc_merger.py
```
Then follow GUI prompts to select files, choose EPC column, and name output.

## 📌 Version
**v1.2** – Cleaned merging logic, faster load, folder-based output, and separate final merger support

---

For future updates (v1.3): consider adding support for master EPC comparison, tagging source devices, and logging merge sessions.
