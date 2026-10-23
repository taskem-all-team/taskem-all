"""Database setup: one engine, one session helper. (~30 LOC)

- File lives in the user's home folder (``~/.taskem/taskem.db``), never in the source tree.
- ``init_db(path=None)`` creates the tables; ``path=":memory:"`` is for tests.
- ``session_scope()`` commits on success, rolls back on error, always closes.
"""

from collections.abc import Iterator
from contextlib import contextmanager

from sqlalchemy.orm import DeclarativeBase, Session


class Base(DeclarativeBase):
    """Parent of every model."""


def init_db(path: str | None = None) -> None:
    # TODO: create the engine + sessionmaker (module-level variables) and Base.metadata.create_all.
    raise NotImplementedError


@contextmanager
def session_scope() -> Iterator[Session]:
    # TODO: yield a Session, commit / rollback / close.
    raise NotImplementedError
