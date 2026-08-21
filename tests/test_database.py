"""Tests for SQLite connection and incidents table creation."""

from gengarileo.database import connect
from gengarileo.schema import init_schema


def test_connect_creates_db_file(tmp_path):
    db_path = tmp_path / "incidents.db"

    conn = connect(db_path)
    try:
        assert db_path.exists()
    finally:
        conn.close()


def test_init_schema_creates_incidents_table(tmp_path):
    db_path = tmp_path / "incidents.db"

    conn = connect(db_path)
    try:
        init_schema(conn)
        row = conn.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'incidents'"
        ).fetchone()
        assert row is not None
        assert row[0] == "incidents"
    finally:
        conn.close()
