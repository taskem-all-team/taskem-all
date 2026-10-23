"""Service tests (no UI). Fill these in as you implement services.py."""

import pytest

from taskem_all import services

pytestmark = pytest.mark.usefixtures("fresh_db")


def test_empty_title_is_rejected() -> None:
    with pytest.raises(ValueError):
        services.add_task("   ")


def test_title_is_trimmed() -> None:
    assert services.add_task("  buy milk ").title == "buy milk"


def test_deleting_project_keeps_tasks() -> None:
    project = services.add_project("Uni")
    task = services.add_task("essay", project_id=project.id)
    services.delete_project(project.id)
    assert services.list_tasks()[0].id == task.id
    assert services.list_tasks()[0].project_id is None


# TODO: done tasks sort last; search matches title; project filter.
