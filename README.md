# EPC Merger & Comparison Tool (v2.0)

A complete Python-based toolkit for automating RFID stocktaking tasks—merging EPC scan data, renaming batches, sorting by format, comparing with master EPC databases, and generating clean reports across readers and locations.

---

## 🔧 Features

### 🧠 Intelligent Batch Merging (`epc_merger.py`)

- Batch-select multiple CSV/Excel scan files
- **Index-based EPC column selection** (choose once per batch)
- Optional:
  - **Prefix filtering** (e.g., only keep EPCs starting with `03`, `01`, etc.)
  - **EPC truncation** (e.g., keep only first 24 characters)
- Automatically extracts:
  - 📍 **Location**
  - 📡 **Reader**
  - 📁 **Source file name**
- ✅ Adds visual tick (✓) to folder name after processing
- Saves merged outputs to `merged/` with timestamped filenames
- Auto-adjusts Excel column widths

### 🔄 Final Cleaned File Merger (`epc_merged_final.py`)

- Merges cleaned Excel files from `merged/`
- Consolidates duplicate EPCs found in multiple locations/readers
- Combines metadata into comma-separated cells
- Optional prefix filtering & truncation
- Saves to `merged_final/` folder

### 📁 Format-Based Sorter (`format_based_sorter.py`)

- Groups scan files into subfolders (`FormatGroup_X`) based on structure
- Prevents merging errors by grouping similar formats
- Only needed for **fixed readers** with multiple file types

### 🏷️ Batch Renaming Tools

- `epc_file_renamer.py`  
  ↳ Select multiple files, preview one, apply uniform `Reader_Location.csv` naming

- `2_file_renamer.py`  
  ↳ Simple tool to add prefix text in front of filenames

### 🧾 Master Database Comparison (`epc_master_comparison.py`)

- Compares merged results against a full master EPC list
- Adds columns:
  - ✅ **Found**
  - 📍 **Location Found**
  - 📡 **Reader Used**
- Generates summary:
  - % of EPCs found
  - Count of duplicates across locations
- Output stored in `comparison_results/`

---

## 🗂 Folder Structure

```
/epc_merger_tool
├── epc_merger.py                  # Batch merger for raw EPC scan files
├── epc_merged_final.py            # Final cleaned EPC file merger
├── format_based_sorter.py         # Sorts raw files by structure
├── epc_master_comparison.py       # Compares merged data vs master EPC list
├── epc_file_renamer.py            # File renamer with preview + pattern
├── 2_file_renamer.py              # Quick prefix-based renamer
├── merged/                        # Folder for intermediate merged files
├── merged_final/                  # Folder for consolidated clean output
├── comparison_results/            # Stores master comparison results
└── README.md                      # This file
```

---

## 🛠 Requirements

- Python 3.10+
- `pandas`
- `openpyxl`
- `tkinter` (included with most Python installations)

Install dependencies:

```bash
pip install pandas openpyxl
```

---

## 🚀 How to Use

### 1. (Optional) Sort by Format

For fixed readers, run:

```bash
python format_based_sorter.py
```

Groups files with similar structure into subfolders.

---

### 2. Rename Files

Choose one of the renaming scripts:

```bash
python epc_file_renamer.py   # Preview & apply formatted naming
python 2_file_renamer.py     # Simple prefix-based batch renamer
```

Ensure filenames follow the `Reader_Location.csv` pattern.

---

### 3. Run the Main Merger

```bash
python epc_merger.py
```

- Select raw scan files
- Choose EPC column
- Apply filtering/truncation if needed
- Files are merged and saved to `merged/`
- Folder will auto-rename with ✓ when done

---

### 4. Merge Final Cleaned Files

```bash
python epc_merged_final.py
```

- Combines cleaned EPC files from `merged/`
- Detects duplicates across different readers/locations
- Saves the output to `merged_final/`

---

### 5. Compare with Master EPC List

```bash
python epc_master_comparison.py
```

- Select merged final file and client master EPC list
- Shows which EPCs were found, where, and by which reader
- Adds Found, Location Found, and Reader Used columns
- Summary results saved in `comparison_results/`

---

## 🧾 Version History

### ✅ v2.0 (Current)

- NEW: Master EPC comparison module (`epc_master_comparison.py`)
- NEW: `comparison_results/` folder for results
- NEW: Two file renamer tools added
- Modular architecture: sort → rename → merge → compare
- Folder ✓ renaming and auto Excel formatting retained

### ✅ v1.6

- Folder tick rename feature
- Auto column sizing in Excel output
- Timestamped file saving in `merged/`

### ✅ v1.5

- Prefix filtering and EPC truncation support
- Final merge deduplication logic
- Format sorter for batch cleanup

---

## 📌 Future Plans

- 📊 Graph generation (adjustable X/Y axis)
- 📋 Excel/PDF summary report export
- 🖥 Convert tool to standalone **.exe** for easier distribution *(priority)*
- 📖 Create illustrated user manual covering:
  - Installation & setup
  - Usage walkthrough
  - File naming rules
  - Troubleshooting guide
