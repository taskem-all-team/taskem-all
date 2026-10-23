"""Both tables in one file. (~35 LOC)

projects: id, name
tasks:    id, title, notes, priority (1 low, 2 medium, 3 high), due_date (nullable),
          done (bool), project_id (nullable FK -> projects.id; NULL = no project)
"""

from sqlalchemy.orm import Mapped, mapped_column

from taskem_all.db import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    # TODO: name


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    # TODO: title, notes, priority, due_date, done, project_id
