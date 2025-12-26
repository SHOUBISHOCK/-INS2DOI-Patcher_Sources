# app.py
# -*- coding: utf-8 -*-
import sys
import os
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from ui.main_window import MainWindow

"""Application entrypoint.

This trimmed build removes the scan/patcher/disabler flows from the GUI,
leaving the Server Spam Blocker tool and the informational launcher.
"""


def _hide_console_window():
    if os.name == "nt":
        try:
            import ctypes
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            if hwnd:
                ctypes.windll.user32.ShowWindow(hwnd, 0)
        except Exception:
            pass
def main():
    _hide_console_window()
    app = QApplication(sys.argv)

    ICON_FILENAME = "INS2DOI Community Patcher.ico"
    base_dir = Path(sys._MEIPASS) if getattr(sys, "frozen", False) else Path(__file__).resolve().parent

    icon_path = base_dir / ICON_FILENAME
    if icon_path.exists():
        app.setWindowIcon(QIcon(str(icon_path)))

    w = MainWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
