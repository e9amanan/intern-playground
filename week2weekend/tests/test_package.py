"""Comprehensive tests covering core logic, parameterization, and CLI routing."""

import pytest
from pathlib import Path
from energy_insights.core import EnergySeries
from energy_insights.exceptions import ValidationError
from energy_insights.cli import main

# --- CORE LOGIC & OOP TESTS ---

@pytest.fixture
def valid_dataset():
    return [
        {"timestamp": "2026-07-15T10:00:00Z", "price": "100.0"},
        {"timestamp": "2026-07-15T11:00:00Z", "price": "200.0"},
        {"timestamp": "2026-07-15T12:00:00Z", "price": "150.0"}
    ]

def test_energy_series_summary(valid_dataset):
    series = EnergySeries(valid_dataset, "price")
    stats = series.summary()
    assert stats["count"] == 3
    assert stats["max"] == 200.0
    assert stats["mean"] == 150.0

# Using parametrize to test edge cases gracefully
@pytest.mark.parametrize("bad_data", [
    [{"timestamp": "2026-07-15T10:00:00Z", "price": "not_a_number"}], # String value
    [{"timestamp": "2026-07-15T10:00:00Z"}],                          # Missing key
    []                                                                # Empty list
])
def test_energy_series_validation(bad_data):
    """Ensures malformed or empty data raises ValidationError."""
    with pytest.raises(ValidationError):
        EnergySeries(bad_data, "price")

# --- CLI TESTS ---

def test_cli_missing_file_exit_code():
    with pytest.raises(SystemExit) as excinfo:
        main(["summary", "--file", "does_not_exist.csv", "--metric", "price"])
    assert "file not found" in str(excinfo.value)

def test_cli_happy_path(tmp_path):
    # Setup temp file
    test_file = tmp_path / "test.csv"
    test_file.write_text("timestamp,price\n2026-07-15T10:00:00Z,150.5\n")
    
    # Run CLI
    exit_code = main(["summary", "--file", str(test_file), "--metric", "price"])
    assert exit_code == 0