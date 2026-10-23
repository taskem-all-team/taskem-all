"""Forecast for a task's due date via Open-Meteo (free, no API key). (~50 LOC)

- Standard library only (``urllib.request`` + ``json``), 5 second timeout.
- One request: daily forecast for the next 16 days for a fixed city, cached in memory.
- Returns ``None`` for dates outside the 16 days, or on ANY error (offline, timeout). The UI
  just hides the weather text; it never shows an error.
- Call it from a ``QThread``/``QRunnable`` so the window never freezes.

Endpoint: https://api.open-meteo.com/v1/forecast?latitude=..&longitude=..
          &daily=weather_code,temperature_2m_max,temperature_2m_min&timezone=auto&forecast_days=16
Credit "Weather data by Open-Meteo.com" must appear somewhere in the UI (e.g. the status bar).
"""

from datetime import date

# TODO: choose the city once (constant is fine to start with; a settings box is optional).
LATITUDE = 44.43
LONGITUDE = 26.10


def get_forecast(day: date) -> str | None:
    """Return a short text like 'Light rain, 8-14 C', or None."""
    raise NotImplementedError
