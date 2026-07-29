import pytest
from datetime import datetime
from week2day5.yourpkg.core import (
    _parse_row,
    clean_data,
    display_daily_averages,
    display_top_spikes,
    display_anomalies,
)
from week2day5.yourpkg.exception import ValidationError


@pytest.fixture
def sample_raw_data():
    """Fixture providing raw CSV row dictionaries."""
    return [
        {"timestamp": "2023-10-01T10:00:00Z", "price": "100.0"},
        {"timestamp": "2023-10-01T11:00:00Z", "price": "150.0"},
    ]


@pytest.fixture
def sample_cleaned_data(sample_raw_data):
    """Fixture providing processed data."""
    return clean_data(sample_raw_data, "price")


# --- Testing _parse_row ---

def test_parse_row_success():
    row = {"timestamp": "2023-10-01T10:00:00Z", "price": "100.0"}
    result = _parse_row(row, "price", 2)
    assert result["value"] == 100.0
    assert isinstance(result["timestamp"], datetime)


def test_parse_row_invalid_data(capsys):
    row = {"timestamp": "2023-10-01T10:00:00Z", "price": "invalid"}
    result = _parse_row(row, "price", 3)
    
    assert result is None
    captured = capsys.readouterr()
    assert "Warning: Skipping invalid row 3" in captured.out


# --- Testing clean_data ---

def test_clean_data_success(sample_raw_data):
    data = clean_data(sample_raw_data, "price")
    assert len(data) == 2


def test_clean_data_empty():
    with pytest.raises(ValidationError, match="No valid data rows found"):
        clean_data([], "price")


def test_clean_data_all_invalid():
    bad_data = [{"timestamp": "2023-10-01", "price": "bad"}]
    with pytest.raises(ValidationError, match="No valid data rows found"):
        clean_data(bad_data, "price")


# --- Testing display functions ---

def test_display_daily_averages(sample_cleaned_data, capsys):
    display_daily_averages(sample_cleaned_data)
    captured = capsys.readouterr()
    assert "23-10-01" in captured.out
    assert "$125.00" in captured.out


def test_display_top_spikes(sample_cleaned_data, capsys):
    display_top_spikes(sample_cleaned_data, top_n=1)
    captured = capsys.readouterr()
    assert "Top 1 price spikes:" in captured.out
    assert "$150.00" in captured.out


@pytest.mark.parametrize("mock_values, expected_output", [
    ([10.0], "Not enough data to calculate standard deviation"), 
    ([10.0, 10.0], "Anomalies detected: 0 as no variance"),
])
def test_display_anomalies_edge_cases(mock_values, expected_output, capsys):
    data = [{"value": v} for v in mock_values]
    display_anomalies(data)
    captured = capsys.readouterr()
    assert expected_output in captured.out


def test_display_anomalies_detection(capsys):
    data = [{"value": 10.0}] * 10 + [{"value": 9999.0}]
    display_anomalies(data)
    captured = capsys.readouterr()
    assert "Anomalies detected: 1 hour(s)" in captured.out