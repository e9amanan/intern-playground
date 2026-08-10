"""Unit tests for pipeline.enrich_task — the TRANSFORM stage, tested in
isolation from extract and load."""

from datetime import datetime

from pipeline import enrich_task


def test_category_count_matches_categories_length():
    task = {"categories": ["Python", "Backend", "SQL"], "due_date_parsed": None}
    result = enrich_task(task)
    assert result["category_count"] == 3


def test_zero_categories():
    task = {"categories": [], "due_date_parsed": None}
    result = enrich_task(task)
    assert result["category_count"] == 0


def test_no_due_date_is_not_overdue():
    task = {"categories": [], "due_date_parsed": None}
    result = enrich_task(task)
    assert result["is_overdue"] is False


def test_past_due_date_is_overdue():
    task = {"categories": [], "due_date_parsed": datetime(2020, 1, 1)}
    result = enrich_task(task, now=datetime(2026, 8, 3))
    assert result["is_overdue"] is True


def test_future_due_date_is_not_overdue():
    task = {"categories": [], "due_date_parsed": datetime(2030, 1, 1)}
    result = enrich_task(task, now=datetime(2026, 8, 3))
    assert result["is_overdue"] is False


def test_due_date_parsed_is_removed_from_output():
    """due_date_parsed is an internal handoff field from the validator;
    it must not leak into the record that gets JSON-dumped or DB-loaded."""
    task = {"categories": [], "due_date_parsed": datetime(2020, 1, 1)}
    result = enrich_task(task, now=datetime(2026, 8, 3))
    assert "due_date_parsed" not in result


def test_enrich_task_mutates_and_returns_same_object():
    task = {"categories": ["A"], "due_date_parsed": None}
    result = enrich_task(task)
    assert result is task