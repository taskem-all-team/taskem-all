"""Start the app: create the database, open the main window. (~15 LOC)"""

import sys

from PyQt6.QtWidgets import QApplication

from taskem_all.db import init_db
from taskem_all.ui.main_window import MainWindow


def main() -> None:
    init_db()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
