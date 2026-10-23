import pytest

from taskem_all.db import init_db


@pytest.fixture
def fresh_db() -> None:
    """Every test gets an empty in-memory database."""
    init_db(":memory:")
