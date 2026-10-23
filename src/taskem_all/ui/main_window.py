"""Main window: two tabs, "Tasks" and "Projects". (~40 LOC)"""

from PyQt6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("taskem-all")
        self.resize(900, 600)
        # TODO: QTabWidget with TasksView and ProjectsView; refresh a view when its tab opens;
        # status bar text "Weather data by Open-Meteo.com".
