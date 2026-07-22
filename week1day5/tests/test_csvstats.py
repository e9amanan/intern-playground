"""
Unit tests for the csv_stats data analysis module.
"""

import pytest

from week1day3.controlflows.csv_stats import load_csv, summarize_numeric, top_n

# --- summarize_numeric Tests ---


def test_summarize_numeric_happy_path():
    """Tests standard min, max, and mean calculations for a valid numeric column."""
    rows = [
        {"name": "Alice", "score": "10"},
        {"name": "Bob", "score": "20"},
        {"name": "Charlie", "score": "30"},
    ]
    result = summarize_numeric(rows, "score")
    assert result == {"min": 10.0, "max": 30.0, "mean": 20.0}


def test_summarize_numeric_empty_rows():
    """Tests that passing an empty list safely returns default 0.0 values."""
    assert summarize_numeric([], "score") == {"min": 0.0, "max": 0.0, "mean": 0.0}


def test_summarize_numeric_missing_column():
    """Tests that a KeyError is raised if the requested column does not exist."""
    rows = [{"name": "Alice", "age": "25"}]
    with pytest.raises(KeyError):
        summarize_numeric(rows, "score")


def test_summarize_numeric_skips_invalid():
    """Tests that invalid or missing strings are safely skipped during math calculations."""
    rows = [{"score": "10"}, {"score": "N/A"}, {"score": "20"}]
    result = summarize_numeric(rows, "score")

    assert result == {"min": 10.0, "max": 20.0, "mean": 15.0}


def test_summarize_numeric_no_valid_data():
    """Tests that a ValueError is raised if the column has zero valid numbers."""
    rows = [{"score": "N/A"}, {"score": "INVALID"}]
    with pytest.raises(ValueError):
        summarize_numeric(rows, "score")


# --- top_n Tests ---


def test_top_n_happy_path():
    """Tests that rows are correctly sorted descending by the specified column."""
    rows = [
        {"id": "1", "val": "10"},
        {"id": "2", "val": "50"},
        {"id": "3", "val": "30"},
    ]
    result = top_n(rows, "val", 2)

    assert len(result) == 2
    assert result[0]["id"] == "2"
    assert result[1]["id"] == "3"


def test_top_n_invalid_data_pushed_to_bottom():
    """Tests that corrupted data is pushed to the bottom of the sorted list."""
    rows = [
        {"id": "1", "val": "10"},
        {"id": "2", "val": "ERROR"},
        {"id": "3", "val": "20"},
    ]
    result = top_n(rows, "val", 3)

    assert result[0]["id"] == "3"
    assert result[1]["id"] == "1"
    assert result[2]["id"] == "2"


# --- load_csv Tests ---


def test_load_csv_file_not_found():
    """Tests that a FileNotFoundError is raised for non-existent files."""
    with pytest.raises(FileNotFoundError):
        load_csv("this_file_does_not_exist.csv")


def test_load_csv_happy_path(tmp_path):
    """Tests that a CSV file is read correctly using a temporary pytest file."""

    fake_csv = tmp_path / "test_data.csv"

    fake_csv.write_text("name,age\nAlice,30\nBob,25", encoding="utf-8")

    result = load_csv(str(fake_csv))

    assert len(result) == 2
    assert result[0]["name"] == "Alice"
    assert result[1]["age"] == "25"
