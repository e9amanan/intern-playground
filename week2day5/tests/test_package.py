"""
Comprehensive tests covering core logic, parameterization, and CLI routing.
"""

import pytest
from yourpkg.cli import main
from week2day5.yourpkg.exception import ValidationError

from week2day5.yourpkg import core

from week2day5.yourpkg import core
from week2day5.yourpkg.cli import main
from week2day5.yourpkg.exception import ValidationError

# --- CORE LOGIC TESTS ---


@pytest.fixture
def valid_dataset():
    """Provide a valid, minimal dataset fixture for testing."""
    return [
        {"timestamp": "2026-07-15T10:00:00Z", "price": "100.0"},
        {"timestamp": "2026-07-15T11:00:00Z", "price": "200.0"},
        {"timestamp": "2026-07-15T12:00:00Z", "price": "150.0"},
    ]


def test_clean_data_valid(valid_dataset):
def test_clean_data_valid():
    """Test that valid data is correctly parsed and values are converted."""
    cleaned = core.clean_data(valid_dataset, "price")
    assert len(cleaned) == 3
    assert cleaned[1]["value"] == 200.0
    assert cleaned[1]["raw_ts"] == "2026-07-15T11:00:00Z"


@pytest.mark.parametrize(
    "bad_data",
    [
        [
            {"timestamp": "2026-07-15T10:00:00Z", "price": "not_a_number"}
        ],  # String value
        [{"timestamp": "2026-07-15T10:00:00Z"}],  # Missing key
        [],  # Empty list
    ],
)
def test_clean_data_validation(bad_data):
    """Ensures malformed or empty data raises a ValidationError."""
    with pytest.raises(ValidationError):
        core.clean_data(bad_data, "price")


# --- CLI TESTS ---


def test_cli_missing_file_exit_code():
    """Test that missing files trigger a SystemExit with the proper message."""
    with pytest.raises(SystemExit) as excinfo:
        main(["analyze", "--file", "does_not_exist.csv", "--metric", "price"])
    assert "not found" in str(excinfo.value).lower()


def test_cli_happy_path(tmp_path):
    """Test a successful CLI run using a valid temporary CSV file."""
    test_file = tmp_path / "test.csv"
    test_file.write_text(
        "timestamp,price\n2026-07-15T10:00:00Z,150.5\n", encoding="utf-8"
    )

    exit_code = main(["analyze", "--file", str(test_file), "--metric", "price"])
    assert exit_code == 0
