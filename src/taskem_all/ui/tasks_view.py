"""The main screen. (~120 LOC)

Search box, project filter, "show done" checkbox, "Add task" button, and a QTableWidget (or
QListWidget) with: done checkbox, title, due date, priority, weather text for the due date.
Double-click a row -> TaskDialog. Delete key / button -> delete_task.
"""

from PyQt6.QtWidgets import QWidget


class TasksView(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        # TODO

    def refresh(self) -> None:
        # TODO: call services.list_tasks(...) with the current search/filter values.
        raise NotImplementedError
