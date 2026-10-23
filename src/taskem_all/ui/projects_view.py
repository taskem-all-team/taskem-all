"""Projects tab. (~60 LOC)

List of projects with "x of y tasks done", an add box and a delete button (ask for
confirmation: "Its tasks will be kept without a project").
"""

from PyQt6.QtWidgets import QWidget


class ProjectsView(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        # TODO

    def refresh(self) -> None:
        raise NotImplementedError
