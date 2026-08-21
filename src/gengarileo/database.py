"""SQLite connection and database path management."""

from __future__ import annotations

import sqlite3
from pathlib import Path

DEFAULT_DB_PATH = Path("data/incidents.db")


def ensure_data_directory(db_path: Path | str) -> None:
    """Create the parent directory for the database file if it is missing."""
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)


def connect(db_path: Path | str | None = None) -> sqlite3.Connection:
    """Open a SQLite connection, creating the data directory if needed."""
    path = DEFAULT_DB_PATH if db_path is None else Path(db_path)
    ensure_data_directory(path)
    return sqlite3.connect(path)
