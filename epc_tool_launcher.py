# epc_tool_launcher.py — onedir-friendly, fast start, correct tool launch

import sys
import os
import subprocess
import runpy
import tkinter as tk
from tkinter import messagebox

# --- ensure Tk submodules get bundled by PyInstaller ---
try:
    import tkinter.filedialog as _tk_filedialog  # noqa: F401
    import tkinter.simpledialog as _tk_simpledialog  # noqa: F401
    import tkinter.messagebox as _tk_messagebox  # noqa: F401
    import tkinter.ttk as _tk_ttk  # noqa: F401
except Exception:
    pass


# ---- EXE resource path helper (works in dev, onefile, and onedir) ----
def resource_path(rel_path: str) -> str:
    if getattr(sys, "frozen", False):
        base = getattr(sys, "_MEIPASS", os.path.dirname(sys.executable))
    else:
        base = os.getcwd()
    return os.path.join(base, rel_path)

# ---- UI colors ----
PURPLE = "#6C29C2"
GRAY = "#BFBFBF"
GREEN = "#C9DC6A"
WHITE = "#FFFFFF"
BG = "#F4F4F4"

# ---- Tool mapping: label → (filename, description) ----
SCRIPTS = {
    "Sort by Format": (
        "format_based_sorter.py",
        "Automatically groups raw scan files into subfolders based on format/header structure.\nUseful for fixed readers producing inconsistent layouts."
    ),
    "Rename Files": (
        "epc_file_renamer.py",
        "Preview and rename multiple files using a consistent naming pattern like Reader_Location.csv.\nHelps ensure metadata can be extracted correctly."
    ),
    "Rename Files (Prefix)": (
        "2_file_renamer.py",
        "Quickly add a prefix (e.g., location, date, reader) to filenames for batch identification.\nSimple and fast for small cleanups."
    ),
    "Merge EPC Batches": (
        "AUTO_SELECT",  # Will be replaced dynamically
        "Batch merge raw RFID scan files using either Reader+Location or just Location, based on checkbox."
    ),
    "Final Merge": (
        "epc_merged_final.py",
        "Merge already-cleaned Excel files and consolidate duplicates across readers or locations.\nSaves to the merged_final/ folder."
    ),
    "Master Comparison": (
        "epc_master_comparison.py",
        "Compare final merged results with a client-provided master EPC list.\nOutputs whether each tag was found, and where."
    )
}

# ---- Child-process entrypoint: run a tool script and exit ----
def _run_tool_from_cli():
    """
    If invoked as:  launcher.exe --run <scriptname.py>
    execute that script's __main__ in this process and then exit.
    Returns True if we handled a tool run (so caller should not show the GUI).
    """
    if len(sys.argv) >= 3 and sys.argv[1] == "--run":
        script_name = sys.argv[2]
        script_path = resource_path(script_name)
        try:
            runpy.run_path(script_path, run_name="__main__")
        except Exception as e:
            # Late import avoids pulling Tk just for CLI errors in case the script itself is CLI
            try:
                from tkinter import messagebox  # noqa: F401
                messagebox.showerror("Tool Error", f"Error running {script_name}:\n{e}")
            except Exception:
                print(f"[Tool Error] {script_name}: {e}", file=sys.stderr)
        return True
    return False

# If called to run a tool, do it and stop (no GUI)
if _run_tool_from_cli():
    sys.exit(0)

# ---- Normal path: show the GUI launcher ----

def run_script(script_name: str):
    """Launch a tool by spawning this same EXE with a --run flag."""
    if script_name == "AUTO_SELECT":
        script_name = "epc_merger_reader.py" if include_reader_var.get() else "epc_merger_location.py"

    # ensure the target is actually present (added via --add-data at build time)
    script_path = resource_path(script_name)
    if not os.path.exists(script_path):
        messagebox.showerror("File Not Found", f"{script_name} was not found next to the launcher.")
        return

    try:
        # Spawn a child of this EXE that will execute the script via runpy (no Python install needed)
        subprocess.Popen([sys.executable, "--run", script_name], shell=False)
    except Exception as e:
        messagebox.showerror("Launch Error", f"Could not launch {script_name}:\n{e}")

def show_description(title, text):
    messagebox.showinfo(title, text)

# ---- GUI ----
root = tk.Tk()
root.attributes("-topmost", True)
root.title("EPC Merger & Comparison Tool")
root.geometry("540x600")
root.configure(bg=BG)
root.resizable(False, False)

tk.Label(root, text="STOCKTAKING TOOLKIT", font=("Segoe UI", 20, "bold"), fg=PURPLE, bg=BG).pack(pady=(30, 10))
tk.Label(root, text="Select a Tool to Launch", font=("Segoe UI", 12), bg=BG).pack(pady=(0, 10))

include_reader_var = tk.BooleanVar(value=False)
tk.Checkbutton(
    root,
    text="Filename includes Reader info (use Reader_Location)",
    variable=include_reader_var,
    font=("Segoe UI", 10),
    bg=BG,
    anchor="w"
).pack(pady=(0, 20))

for label, (script, desc) in SCRIPTS.items():
    frame = tk.Frame(root, bg=BG)
    frame.pack(pady=6)

    tk.Button(
        frame,
        text=label,
        width=28,
        height=2,
        bg=PURPLE,
        fg=WHITE,
        font=("Segoe UI", 10, "bold"),
        activebackground=GREEN,
        activeforeground="#000000",
        command=lambda s=script: run_script(s)
    ).pack(side="left", padx=(0, 6))

    tk.Button(
        frame,
        text="❓",
        width=3,
        height=2,
        bg=GRAY,
        fg="#000000",
        font=("Segoe UI", 10, "bold"),
        command=lambda t=label, d=desc: show_description(t, d)
    ).pack(side="left")

tk.Button(
    root,
    text="❌ Quit",
    width=34,
    height=2,
    bg="#D9534F",
    fg=WHITE,
    font=("Segoe UI", 10, "bold"),
    command=root.quit
).pack(pady=25)

root.mainloop()
