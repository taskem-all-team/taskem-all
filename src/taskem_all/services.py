"""All the logic, no UI code. (~80 LOC)

Rules:
- Validate here, not in widgets: a task title is trimmed and must not be empty (ValueError).
- Deleting a project keeps its tasks (project_id becomes NULL).
- Each function opens its own ``session_scope()``.
"""

from datetime import date

from taskem_all.models import Project, Task

# ---- tasks ----


def add_task(
    title: str,
    *,
    priority: int = 2,
    due_date: date | None = None,
    project_id: int | None = None,
    notes: str = "",
) -> Task:
    raise NotImplementedError


def update_task(task_id: int, **changes: object) -> Task:
    raise NotImplementedError


def set_done(task_id: int, done: bool) -> None:
    raise NotImplementedError


def delete_task(task_id: int) -> None:
    raise NotImplementedError


def list_tasks(
    search: str = "", project_id: int | None = None, show_done: bool = True
) -> list[Task]:
    """Sorted: not done first, then by due date (no date last), then priority."""
    raise NotImplementedError


# ---- projects ----


def add_project(name: str) -> Project:
    raise NotImplementedError


def delete_project(project_id: int) -> None:
    raise NotImplementedError


def list_projects() -> list[Project]:
    raise NotImplementedError
