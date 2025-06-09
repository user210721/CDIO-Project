# EPC Merger Tool (v1.5)

A Python-based toolkit to streamline RFID stocktaking by merging EPC scan data, detecting duplicates, extracting metadata, and consolidating tagged item tracking across readers and locations.

---

## 🔧 Features

### 🧠 Intelligent Batch Merging (`epc_merger.py`)

* Select multiple CSV/Excel files in **batches**
* **Index-based EPC column selection** (select once per batch)
* Consistent structure assumption within each batch
* Supports **truncating EPCs** (e.g., first 24 characters)
* Optional **prefix filtering** (e.g., only keep EPCs starting with `03`, `E888`)
* Automatically extracts:

  * 📍 **Location**
  * 🛁 **Reader**
  * 📁 **Source file name**
* Saves merged outputs to the `merged/` folder with timestamped filenames
* Auto-adjusts Excel column widths

### 🔄 Final Merger (`epc_merged_file_merger.py`)

* Load previously merged files from `merged/`
* Optional **EPC prefix filtering** and **truncation**
* Detects **duplicate EPCs found at multiple locations or readers**:

  * Combines locations/readers into a single cell (comma-separated)
* Saves final output to the `merged_final/` folder

### 📂 Format-Based Sorting Tool

* Automatically sorts raw RFID scan files into folders based on format structure
* Prevents batch errors by keeping similar file layouts together
* ✅ Only needed for readers that generate **both unique tag files and all tags scanned files** (e.g., Fixed Readers)

---

## 🗂 File Structure

```
/epc_merger_tool
├── epc_merger.py                # Main raw scan merger
├── epc_merged_file_merger.py   # Final cleaned file merger
├── format_sorter.py             # Sorts raw files by format
├── merged/                      # Intermediate merged output files
├── merged_final/               # Final consolidated output
└── README.md                   # This file
```

---

## 🛠 Requirements

* Python 3.10+
* `pandas`
* `openpyxl`
* `tkinter` (bundled with most Python distributions)

Install dependencies (if needed):

```bash
pip install pandas openpyxl
```

---

## 🚀 How to Use

### 1. Sort by Format (Fixed Readers Only)

> 📌 Skip if using handheld scanners — they output a consistent format.

Run the format sorter:

```bash
python format_sorter.py
```

This groups files with the same structure into subfolders in the same directory.

---

### 2. Rename Files

Use the EPC File Renamer (separate script) to rename files consistently as:

```
[Reader]_[Location]_x.csv
e.g. FixedReader_GulDrive_1.csv
```

---

### 3. Run the Main Merger

```bash
python epc_merger.py
```

* Select files for each batch
* Choose the EPC column once
* Optionally filter by prefix or truncate EPCs
* Add multiple batches
* Save to `merged/`

---

### 4. Run the Final Merger

```bash
python epc_merged_file_merger.py
```

* Select previously merged files
* Optional filtering & truncation
* Consolidates duplicate EPCs across locations/readers
* Saves output to `merged_final/`

---

## 📌 Version History

### ✅ v1.5 (Current)

* **Prefix filtering** supports comma-separated values (`03, 01`)
* **EPC truncation** (e.g. first 24 chars)
* **Duplicate location & reader detection** merged into single cells
* Final merger fully supports smart consolidation
* Added format sorter for readers with mixed file types

### ✅ v1.4

* Added `format_sorter.py` to group files with same layout
* EPC Renamer script (external) used for standardizing filenames
* Visual cleanups and prompt clarifications

### ✅ v1.3

* Smart delimiter fallback (comma → tab)
* Header detection instead of `csv.Sniffer()`
* Faster file preview loading (10 rows)
* Batch column position reuse

---

## ✨ Future Plans

* Master EPC vs scanned EPC comparison with full tick & summary
* Visual dashboards: tag coverage %, tags per reader
* PDF report generation

---
