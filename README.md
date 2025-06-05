# EPC Merger Tool (v1.4)

A Python-based tool for merging RFID scan files and reconciling EPCs across different locations and readers. Designed for stocktaking workflows, especially where large batches of scanned files are handled.

---

## 🔧 Features

### 🧠 Intelligent Batch Merging
- Select multiple CSV/Excel files per batch
- Select EPC column once; applies to all files in batch by column index
- Handles inconsistent column headers automatically (smart row start detection)

### 🎯 Prefix-Based EPC Filtering
- Option to filter EPCs by prefix (e.g. `03`, `E888`, `01`)
- Add multiple prefixes in one session
- Applies during both batch merge and final merge

### ⚡ Fast & Robust
- Skips broken or empty files gracefully
- Removed `csv.Sniffer()` (improved performance and reliability)
- Reads only first few rows for preview, not entire file

### 🏷️ Metadata Extraction
- Extracts `Reader`, `Location`, and `File Name` from filenames (e.g. `Fixed Reader_Gul Drive_1.csv`)
- Adds them as columns to merged data

### 📏 Excel Auto-Fit Columns
- Output Excel columns auto-fit based on content length
- Improves readability of EPC, Reader, and Location fields

### 💾 Clean Output
- Outputs saved to `merged/` folder
- Prompts user to name each merged file
- Prevents overwrites with timestamped default filenames

### 🔁 Final Merger Tool
- A separate script for combining previously merged files
- Retains all metadata columns (`Reader`, `Location`, etc.)
- Output saved in `merged_final/`
- Same prefix filtering and autosizing support included

### 🧯 Save Safety
- Prevents crash if output file is already open in Excel
- Prompts user to close the file instead of throwing a `PermissionError`

### 🗂️ v1.4 File Format Sorter (NEW)
- New standalone utility script that scans and groups RFID scan files into folders based on format structure
- Classifies files as:
  - `Format_RFID` (tag tables)
  - `Format_Raw_EPC` (simple EPC lists)
  - `Format_Unknown`
- ⚠️ Only needed for readers that generate both 'unique tag files' and all 'tags scanned files', not needed for current handheld reader

---

## 📁 File Structure
```
/epc_merger_tool
├── epc_merger.py              # Main merging tool (raw scan merging)
├── epc_merged_final.py        # Final merger for cleaned files
├── format_based_sorter.py     # NEW: Sorts files by structure
├── merged/                    # Intermediate merged batches
├── merged_final/              # Final consolidated output
└── README.md                  # This file
```

---

## 🛠 Requirements
- Python 3.10+
- `pandas`
- `openpyxl`
- `tkinter` (included with most Python distributions)

Install requirements:
```bash
pip install pandas openpyxl
```

---

## 🚀 How to Run
```bash
python epc_merger.py
```
Then follow the GUI prompts to:
- Select a batch of scan files
- Choose the EPC column
- Optionally enter EPC prefixes
- Name the output Excel file

To merge cleaned batches:
```bash
python epc_merged_final.py
```

To group files by format before merging:
```bash
python format_based_sorter.py
```
(Only necessary for readers that generate both unique tag files and all tags scanned files)

---

## 📌 Version
**v1.4** – Added format-based sorting tool, refined prefix filtering, improved empty file detection and cleanup for structured batch processing.

---

## 🧪 Coming Soon (Ideas)
- Master EPC database comparison
- EPC source tracing by device
- Config file for reusable settings
- Merge session logging
