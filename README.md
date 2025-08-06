# EPC Merger & Comparison Tool (v2.1)

A complete Python-based toolkit for automating **RFID stocktaking workflows**—merging scan data, renaming batches, sorting formats, comparing with master databases, and generating clean reports across readers and locations.

---

## 🔧 Features

### 🧠 Intelligent Batch Merging (`epc_merger_location.py` / `epc_merger_reader.py`)

- Select folder or individual files for merging
- ✅ **Smart EPC Column Detection**:
  - Auto-detects columns with 4–32 char hex-like values
  - Shows preview (1st to 3rd rows) for easy selection
- ✅ **Auto-extracts metadata from filename**:
  - 📍 Location ONLY 
  OR
  - 📡 Reader And Location (File Name Format: Reader_Location)
- ✅ **De-duplicates with smart merging**:
  - If same EPC but different values: combines non-`Unknown` values into comma-separated format
- ✅ Excel output auto-sizes columns
- ✅ Handles mismatched headers between files
- ✅ Saves with timestamps to `merged/`

Optional:
- 🔍 Prefix filtering (e.g. only EPCs starting with `03`, `01`)
- ✂️ EPC truncation (e.g. keep first 24 characters)

---

### 📁 Final EPC File Merger (`epc_merged_final.py`)

- Merges all files from `merged/`
- Combines duplicate EPCs across files/readers/locations
- Consolidates metadata intelligently
- Applies optional filters
- Saves clean output to `merged_final/`

---

### 🔍 Master EPC Comparison (`epc_master_comparison.py`)

- Compares merged output with master EPC file(s)
- Adds columns:
  - ✅ Found
  - 📍 Location Found
  - 📡 Reader Used (OPTIONAL)
- Auto-sizes Excel output
- Handles multiple master files (processes separately)
- Generates summary with:
  - % EPCs found
  - Total duplicates detected
- Saves to `comparison_results/`

---

### 🗂 Format-Based Sorter (`format_based_sorter.py`)

- Groups files into subfolders (`FormatGroup_X`) based on:
  - Column count
  - Header structure
- Helps manage inconsistent file formats from fixed readers
- Auto-deletes empty or unsupported files

---

### 🏷️ File Renaming Tools

- `epc_file_renamer.py`  
  ↳ Rename multiple files with uniform pattern (e.g. `Reader_Location.csv` OR 'Location.csv') via preview dialog

- `2_file_renamer.py`  
  ↳ Quickly add prefixes to filenames (e.g. warehouse, date, etc.)

---

## 🗂 Folder Structure

```
/epc_merger_tool
├── epc_merger_location.py                  # Location-based EPC merger
├── epc_merger_reader.py          # Reader + Location EPC merger
├── epc_merged_final.py           # Final clean output merger
├── epc_master_comparison.py      # Master database comparison tool
├── format_based_sorter.py        # File grouping by structure
├── epc_file_renamer.py           # Full pattern-based renamer
├── 2_file_renamer.py             # Prefix-only renamer
├── merged/                       # Output of initial EPC merge
├── merged_final/                 # Final cleaned merged files
├── comparison_results/           # Results from master comparison
└── README.md                     # You're reading it
```

---

## ⚙️ Requirements

- Python 3.10+
- Dependencies:
  - `pandas`
  - `openpyxl`
  - `tkinter` (preinstalled with Python)
  - `xlrd` (for older Excel formats)

Install with:

```bash
pip install pandas openpyxl xlrd
```

---

## 🚀 How to Use

### 1. (Optional) Sort Raw Files by Format

```bash
python format_based_sorter.py
```

Organizes inconsistent files into format-specific folders.

---

### 2. Rename Files

Choose one tool:

```bash
python epc_file_renamer.py   # Preview & unified pattern renaming
python 2_file_renamer.py     # Simple prefix-based rename
```

Use format: 'Location.csv' OR `Reader_Location.csv` for best results.

---

### 3. Merge Raw EPC Files

```bash
python epc_merger_reader.py  # If filenames include Reader + Location
# or
python epc_merger_location.py         # If filenames include only Location
```

- Choose folder or files
- Select EPC column from preview
- Output is saved in `merged/✓_foldername_<timestamp>.xlsx`

---

### 4. Merge Final EPC Files

```bash
python epc_merged_final.py
```

Combines all cleaned EPC files from `merged/` into one master.

---

### 5. Compare Against Master Database

```bash
python epc_master_comparison.py
```

- Select final merged EPC file + master list(s)
- Adds Found, Location Found, Reader Used
- Summary + result files saved to `comparison_results/`

---

## 📚 Version History

### ✅ v2.1 (Current)

- 🔍 Smart EPC column detection added (hex detection + preview dropdown)
- 🧠 Merging logic now combines conflicting non-unknown values
- 📄 File merging now handles missing columns across files
- ✅ File name column no longer added unless present
- 📊 Master comparison now includes:
  - % EPCs found
  - Total duplicates
  - Excel formatting improvements
- 🛠 All scripts structured for `.exe` GUI integration

### ✅ v2.0

- Full toolkit modular release
- Master comparison script added
- File renaming tools (with and without preview)
- Format sorter
- Timestamped output
- Folder tick rename logic
- Excel autosizing

### ✅ v1.6

- Added ✓ to merged folders
- Excel column autosizing
- Timestamped filenames in `merged/`

### ✅ v1.5

- Prefix filtering + EPC truncation
- Format-based file sorter
- Final deduplication script

---

## 📌 Roadmap

- 📊 EPC dashboard + visual graphs
- 🧾 PDF & Excel summary exports
- 🖥 `.exe` GUI launcher for all tools (in development)
- 📘 Illustrated user guide:
  - Installation
  - Tagging SOP
  - Troubleshooting
  - File naming rules
- 🧪 Interactive EPC validation tool (coming soon)

---

## 💡 Project Info

Developed for streamlining **RFID stocktaking operations** across large-scale deployments. Built for reusability across clients, modular workflows, and full automation of common tagging SOPs.

---
