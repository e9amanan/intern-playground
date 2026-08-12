"""Integration-level tests for etl_pipeline() — wiring extract -> transform
-> load together, plus the top-level error path. Component behavior is
already covered separately in test_validators.py / test_transform.py /
test_load.py; these confirm they're actually connected correctly."""

import json
import sqlite3
from unittest.mock import patch

from pipeline import etl_pipeline


def test_end_to_end_happy_path(tmp_path, csv_file, monkeypatch):
    monkeypatch.chdir(tmp_path)
    csv_path = csv_file(
        "title,description,status,categories,due_date\n"
        'Setup Django,Initial config,done,"Python,Backend",2020-08-01\n'
    )
    db_path = str(tmp_path / "out.db")
    json_path = str(tmp_path / "out.json")

    etl_pipeline(csv_path, db_path, json_path)

    with sqlite3.connect(db_path) as conn:
        row = conn.execute(
            "SELECT title, category_count, is_overdue FROM tasks"
        ).fetchone()
    assert row == ("Setup Django", 2, 1)

    with open(json_path) as f:
        data = json.load(f)
    assert data[0]["title"] == "Setup Django"
    assert "due_date_parsed" not in data[0]


def test_no_valid_rows_exits_without_touching_db(
    tmp_path, csv_file, monkeypatch, capsys
):
    monkeypatch.chdir(tmp_path)
    csv_path = csv_file(
        "title,description,status,categories,due_date\n" ",bad,todo,X,\n"
    )
    db_path = str(tmp_path / "out.db")

    etl_pipeline(csv_path, db_path)

    captured = capsys.readouterr()
    assert "No valid data to load" in captured.out
    import os

    assert not os.path.exists(db_path)


def test_load_failure_is_caught_and_reported(tmp_path, csv_file, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    csv_path = csv_file(
        "title,description,status,categories,due_date\n" "Task,desc,todo,Python,\n"
    )
    db_path = str(tmp_path / "out.db")

    with patch("pipeline.load_to_sqlite", side_effect=sqlite3.OperationalError("boom")):
        etl_pipeline(csv_path, db_path)

    captured = capsys.readouterr()
    assert "CRITICAL ERROR during LOAD" in captured.out
    assert "rolled back" in captured.out
