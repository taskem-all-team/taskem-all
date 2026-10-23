"""Add / edit a task. (~60 LOC)

Fields: title, notes, priority, optional due date, project. Shows the weather text for the
chosen date. Show the ValueError message from services if the title is empty.
"""

from PyQt6.QtWidgets import QDialog, QWidget


class TaskDialog(QDialog):
    def __init__(self, parent: QWidget | None = None, task_id: int | None = None) -> None:
        super().__init__(parent)
        # TODO

    def get_values(self) -> dict[str, object]:
        """Fields in the shape services.add_task / update_task expect."""
        raise NotImplementedError
