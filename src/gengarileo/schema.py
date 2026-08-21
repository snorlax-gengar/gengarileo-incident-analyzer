"""SQLite schema definitions and initialization."""

import sqlite3

CREATE_INCIDENTS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL
);
"""


def init_schema(conn: sqlite3.Connection) -> None:
    """Create the incidents table if it does not already exist."""
    conn.execute(CREATE_INCIDENTS_TABLE_SQL)
    conn.commit()
