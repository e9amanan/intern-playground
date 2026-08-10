"""Unit tests for pipeline.load_to_sqlite / load_to_json — the LOAD stage,
tested in isolation from extract and transform. Uses a real (but disposable,
tmp_path-backed) SQLite DB rather than mocking the cursor, since sqlite3
against a temp file is fast, deterministic, and tests real SQL correctness
rather than the shape of our own mock."""

import json
import sqlite3

import pytest

from pipeline import load_to_json, load_to_sqlite


def _tasks(n_categories_per_task):
    """Build n enriched task dicts, task i gets n_categories_per_task[i] cats."""
    out = []
    for i, n in enumerate(n_categories_per_task):
        out.append(
            {
                "title": f"Task {i}",
                "description": "desc",
                "status": "todo",
                "categories": [f"Cat{c}" for c in range(n)],
                "category_count": n,
                "is_overdue": False,
            }
        )
    return out


def test_single_task_no_categories_inserts_one_row(empty_db):
    load_to_sqlite(_tasks([0]), empty_db)
    with sqlite3.connect(empty_db) as conn:
        rows = conn.execute("SELECT title FROM tasks").fetchall()
        junctions = conn.execute("SELECT * FROM tasks_categories").fetchall()
    assert rows == [("Task 0",)]
    assert junctions == []


def test_task_with_categories_creates_junction_rows(empty_db):
    load_to_sqlite(_tasks([2]), empty_db)
    with sqlite3.connect(empty_db) as conn:
        cats = conn.execute("SELECT name FROM categories ORDER BY name").fetchall()
        junctions = conn.execute("SELECT * FROM tasks_categories").fetchall()
    assert cats == [("Cat0",), ("Cat1",)]
    assert len(junctions) == 2


def test_shared_category_is_not_duplicated(empty_db):
    """Two tasks sharing 'Cat0' should produce ONE categories row, not two —
    this is the N+1 bug the optimization fixes: without the id cache the
    original code would still work correctly here, but would issue a
    redundant SELECT for 'Cat0' on the second task instead of reusing it."""
    tasks = _tasks([1, 1])  
    load_to_sqlite(tasks, empty_db)
    with sqlite3.connect(empty_db) as conn:
        cats = conn.execute("SELECT name FROM categories").fetchall()
        junctions = conn.execute("SELECT * FROM tasks_categories").fetchall()
    assert cats == [("Cat0",)]
    assert len(junctions) == 2  


def test_empty_task_list_is_a_noop(empty_db):
    load_to_sqlite([], empty_db)
    with sqlite3.connect(empty_db) as conn:
        rows = conn.execute("SELECT * FROM tasks").fetchall()
    assert rows == []


def test_invalid_status_raises_and_is_not_partially_committed(empty_db):
    """CHECK(status IN (...)) should reject a bad status. The caller
    (etl_pipeline) is responsible for catching this and rolling back;
    here we confirm the constraint itself actually fires."""
    tasks = _tasks([0])
    tasks[0]["status"] = "not_a_real_status"
    with pytest.raises(sqlite3.IntegrityError):
        load_to_sqlite(tasks, empty_db)


def test_load_to_json_writes_expected_content(tmp_path):
    path = str(tmp_path / "out.json")
    data = [{"title": "A", "categories": ["X"]}]
    load_to_json(data, path)
    with open(path) as f:
        loaded = json.load(f)
    assert loaded == data


def test_load_to_json_default_path(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    load_to_json([{"title": "A"}])
    assert (tmp_path / "validated_tasks.json").exists()