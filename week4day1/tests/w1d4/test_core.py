import pytest

from week1day4.energy_insights.core import compute_daily_averages, find_spikes


@pytest.fixture
def sample_energy_data():
    "sample data"
    return [
        {"timestamp": "2023-01-01 08:00:00", "power": "100.0"},
        {"timestamp": "2023-01-01 12:00:00", "power": "200.0"},
        {"timestamp": "2023-01-02 09:00:00", "power": "150.0"},
        {"timestamp": "2023-01-02 11:00:00", "power": "invalid"},
        {"timestamp": "2023-01-03 10:00:00", "power": ""},
    ]


def test_compute_daily_averages(sample_energy_data):
    "daily average test"
    result = compute_daily_averages(sample_energy_data, "timestamp", "power")

    assert result == {"2023-01-01": 150.0, "2023-01-02": 150.0}


def test_compute_daily_averages_missing_column(sample_energy_data):
    "test that a value error is raised"
    with pytest.raises(KeyError):
        compute_daily_averages(sample_energy_data, "bad_timestamp_col", "power")


def test_compute_daily_averages_no_valid_data():
    bad_data = [{"timestamp": "2023-01-01", "power": "invalid"}]
    with pytest.raises(ValueError, match="No valid numeric data"):
        compute_daily_averages(bad_data, "timestamp", "power")


def test_find_spikes(sample_energy_data):
    "test that top N spikes are identical and sorted"
    spikes = find_spikes(sample_energy_data, "power", top=2)

    assert len(spikes) == 2
    assert spikes[0]["power"] == "200.0"
    assert spikes[1]["power"] == "150.0"


def test_find_spikes_missing_column(sample_energy_data):
    "test KeyError for spikes"
    with pytest.raises(KeyError):
        find_spikes(sample_energy_data, "missing_col", top=2)
