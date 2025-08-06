import os
from tkinter import filedialog, Tk, simpledialog, Toplevel, Label

def show_loading_popup():
    popup = Toplevel()
    popup.title("Renaming...")
    popup.geometry("300x80")
    popup.attributes("-topmost", True)
    Label(popup, text="Renaming files, please wait...").pack(pady=20)
    popup.update()
    return popup

def rename_files(file_paths, prefix):
    popup = show_loading_popup()

    for file_path in file_paths:
        folder, original_name = os.path.split(file_path)
        new_name = f"{prefix}_{original_name}"
        new_path = os.path.join(folder, new_name)
        try:
            os.rename(file_path, new_path)
            print(f"Renamed: {original_name} -> {new_name}")
        except Exception as e:
            print(f"❌ Failed to rename {original_name}: {e}")

    print("Renaming completed.")
    popup.destroy()

# Main
root = Tk()
root.withdraw()

file_paths = filedialog.askopenfilenames(title="Select files to rename")

if not file_paths:
    print("No files selected.")
    exit()

prefix = simpledialog.askstring("Input", "Enter text to add as prefix:")

if prefix:
    rename_files(file_paths, prefix)
else:
    print("No prefix entered. Renaming cancelled.")
