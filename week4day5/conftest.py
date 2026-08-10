import sqlite3

import pytest

from week4day2.database_practice import setup_database


@pytest.fixture
def csv_file(tmp_path):
    """Factory fixture: write a small CSV with given rows, return its path."""

    def _make(rows: str) -> str:
        p = tmp_path / "input.csv"
        p.write_text(rows)
        return str(p)

    return _make


@pytest.fixture
def valid_task():
    """A single already-validated, already-enriched-ready task dict."""
    return {
        "title": "Write tests",
        "description": "Cover the ETL pipeline",
        "status": "todo",
        "categories": ["Python", "Testing"],
        "due_date": None,
        "due_date_parsed": None,
    }


@pytest.fixture
def empty_db(tmp_path):
    """A fresh SQLite DB with the real schema applied, ready for load tests."""
    db_path = str(tmp_path / "test.db")
    setup_database(db_path)
    return db_path