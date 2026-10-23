# Plan

Deadlines: enroll on Moodle by **Nov 4**, architecture doc **Nov 18**, feature freeze
**Nov 28**, submit **Dec 3**.

| Week | Dev A (db, logic) | Dev B (UI) |
|---|---|---|
| Oct 23 - Nov 5 | db.py, models.py, services.py + tests | main window, tasks view, task dialog |
| Nov 6 - 19 | weather.py; architecture doc (together) | projects view, weather text in list/dialog |
| Nov 20 - Dec 3 | bug fixes, README | polish, screenshots |

Cut order if behind: weather text -> projects tab. Never cut: tasks, search, saving to disk.

## Design decisions

- Layers: UI -> services.py -> models/db. Widgets never touch the database.
- `done` is a simple boolean. Priority is 1-3. No statuses, no Kanban, no calendar.
- Weather never blocks or breaks the UI: any failure means "no weather text".
- Tests use an in-memory SQLite database.

## Architecture doc outline (due Nov 18)

1. Introduction: idea, users, features. 2. Overview: UI -> services -> SQLite (+ Open-Meteo).
3. Components: db/models, services, weather, UI. 4. Running and testing. 5. Conclusions: hours, what we learned.
