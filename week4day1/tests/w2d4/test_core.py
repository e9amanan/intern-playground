from datetime import datetime

import pytest

from week2day4.cli_project.yourpkg.core import (
    clean_data,
    display_anomalies,
    display_daily_averages,
    display_top_spikes,
)
from week2day4.cli_project.yourpkg.exceptions import ValidationError


@pytest.fixture
def sample_raw_data():
    """Fixture providing raw CSV row dictionaries."""
    return [
        {"timestamp": "2023-10-01T10:00:00Z", "price": "100.0"},
        {"timestamp": "2023-10-01T11:00:00Z", "price": "150.0"},
        {"timestamp": "2023-10-02T10:00:00Z", "price": "invalid"},  # Should be skipped
    ]


@pytest.fixture
def sample_cleaned_data(sample_raw_data):
    """Fixture providing processed data."""
    return clean_data(sample_raw_data[:2], "price")


# --- Testing clean_data ---


def test_clean_data_success(sample_raw_data):
    data = clean_data(sample_raw_data, "price")
    assert len(data) == 2
    assert isinstance(data[0]["timestamp"], datetime)
    assert data[0]["value"] == 100.0


def test_clean_data_empty():
    with pytest.raises(ValidationError, match="No valid data rows found"):
        clean_data([], "price")


def test_clean_data_missing_metric(sample_raw_data):
    with pytest.raises(ValidationError, match="No valid data rows found"):
        # Passing a metric column that doesn't exist
        clean_data(sample_raw_data, "non_existent_column")


# --- Testing display functions ---


def test_display_daily_averages(sample_cleaned_data, capsys):
    display_daily_averages(sample_cleaned_data)
    captured = capsys.readouterr()

    # Avg of 100 and 150 is 125
    assert "23-10-01" in captured.out
    assert "$125.00" in captured.out


def test_display_top_spikes(sample_cleaned_data, capsys):
    display_top_spikes(sample_cleaned_data, top_n=1)
    captured = capsys.readouterr()

    assert "Top 1 price spikes:" in captured.out
    assert "2023-10-01T11:00:00Z" in captured.out
    assert "$150.00" in captured.out


@pytest.mark.parametrize(
    "mock_values, expected_output",
    [
        ([10.0], "Not enough data to calculate standard deviation"),  # < 2 items
        ([10.0, 10.0, 10.0], "Anomalies detected: 0 as no variance"),  # 0 std dev
    ],
)
def test_display_anomalies_edge_cases(mock_values, expected_output, capsys):
    data = [{"value": v} for v in mock_values]
    display_anomalies(data)
    captured = capsys.readouterr()
    assert expected_output in captured.out


def test_display_anomalies_detection(capsys):
    # 10 normal values, 1 extreme outlier (anomaly)
    data = [{"value": 10.0}] * 10 + [{"value": 9999.0}]
    display_anomalies(data)
    captured = capsys.readouterr()
    assert "Anomalies detected: 1 hour(s)" in captured.out
