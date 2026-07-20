"""
Unit tests for the energy_insights core module.
"""

import pytest
from energy_insights.core import compute_daily_averages, find_spikes

# --- compute_daily_averages Tests ---


def test_compute_daily_averages_happy_path():
    """Tests that daily averages are computed correctly for valid data."""
    rows = [
        {"timestamp": "2026-07-09 10:00", "price": "50.0"},
        {"timestamp": "2026-07-09 14:00", "price": "150.0"},
        {"timestamp": "2026-07-10 09:00", "price": "100.0"},
    ]
    result = compute_daily_averages(rows, "timestamp", "price")

    # 2026-07-09 average is (50 + 150) / 2 = 100.0
    assert result["2026-07-09"] == 100.0
    assert result["2026-07-10"] == 100.0


def test_compute_daily_averages_skips_bad_data():
    """Tests that invalid or missing numeric data is safely skipped."""
    rows = [
        {"timestamp": "2026-07-09 10:00", "price": "50.0"},
        {"timestamp": "2026-07-09 12:00", "price": "N/A"},
        {"timestamp": "2026-07-09 14:00", "price": "150.0"},
    ]
    result = compute_daily_averages(rows, "timestamp", "price")
    assert result["2026-07-09"] == 100.0


def test_compute_daily_averages_missing_column():
    """Tests that a KeyError is raised when the required column is missing."""
    rows = [{"timestamp": "2026-07-09 10:00", "cost": "50.0"}]
    with pytest.raises(KeyError):
        compute_daily_averages(rows, "timestamp", "price")


def test_compute_daily_averages_no_valid_data():
    """Tests that a ValueError is raised when no valid data is found."""
    rows = [{"timestamp": "2026-07-09", "price": "invalid"}]
    with pytest.raises(ValueError):
        compute_daily_averages(rows, "timestamp", "price")


# --- find_spikes Tests ---


def test_find_spikes_happy_path():
    """Tests that spikes are correctly identified and returned in order."""
    rows = [
        {"id": "1", "usage": "10.5"},
        {"id": "2", "usage": "99.9"},
        {"id": "3", "usage": "45.0"},
    ]
    result = find_spikes(rows, "usage", 2)

    assert len(result) == 2
    assert result[0]["id"] == "2"
    assert result[1]["id"] == "3"


def test_find_spikes_handles_invalid_data():
    """Tests that invalid data is pushed to the bottom of the sorted spikes."""
    rows = [
        {"id": "1", "usage": "100.0"},
        {"id": "2", "usage": "ERROR"},
        {"id": "3", "usage": "50.0"},
    ]
    result = find_spikes(rows, "usage", 3)

    assert result[0]["id"] == "1"
    assert result[1]["id"] == "3"
    assert result[2]["id"] == "2"


def test_find_spikes_missing_column():
    """Tests that a KeyError is raised when the sort column is missing."""
    rows = [{"id": "1", "usage": "100.0"}]
    with pytest.raises(KeyError):
        find_spikes(rows, "wrong_column", 1)
