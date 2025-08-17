# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['epc_tool_launcher.py'],
    pathex=[],
    binaries=[],
    datas=[('format_based_sorter.py', '.'), ('epc_file_renamer.py', '.'), ('2_file_renamer.py', '.'), ('epc_merger_reader.py', '.'), ('epc_merger_location.py', '.'), ('epc_merged_final.py', '.'), ('epc_master_comparison.py', '.')],
    hiddenimports=['pandas', 'numpy', 'openpyxl', 'tzdata', 'tkinter.filedialog', 'tkinter.simpledialog', 'tkinter.ttk', 'tkinter.messagebox'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='epc_tool_launcher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='epc_tool_launcher',
)
