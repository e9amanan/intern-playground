from unittest.mock import mock_open, patch

import pytest

from week2day4.cli_project.yourpkg.cli import handle_analyze, main
from week2day4.cli_project.yourpkg.exceptions import FileProcessingError


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="timestamp,price\n2023-10-01T10:00:00Z,50.0",
)
def test_main_analyze_success(mock_file, capsys):
    """Test full successful execution of the analyze command."""
    # Simulating CLI arguments: `yourpkg analyze -f dummy.csv -m price -t 1`
    test_args = ["analyze", "-f", "dummy.csv", "-m", "price", "-t", "1"]

    exit_code = main(test_args)

    assert exit_code == 0
    mock_file.assert_called_once_with("dummy.csv", "r", encoding="utf-8")

    captured = capsys.readouterr()
    assert "Daily averages:" in captured.out
    assert "Top 1 price spikes:" in captured.out


@patch("builtins.open")
def test_handle_analyze_file_not_found(mock_file):
    """Test that a missing file correctly raises a SystemExit."""
    # Force the mock open() to raise a FileNotFoundError
    mock_file.side_effect = FileNotFoundError

    # We must mock the argparse Namespace object that `handle_analyze` expects
    class DummyArgs:
        file = "missing.csv"
        metric = "price"
        top = 3

    # Catch the sys.exit call
    with pytest.raises(
        SystemExit, match="File Error: The file 'missing.csv' was not found."
    ):
        handle_analyze(DummyArgs())


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="timestamp,wrong_column\n2023-10-01,50.0",
)
def test_handle_analyze_validation_error(mock_file):
    """Test that passing invalid CSV headers triggers a SystemExit due to validation failure."""

    class DummyArgs:
        file = "bad_data.csv"
        metric = "price"  # This metric doesn't exist in the mocked CSV
        top = 3

    with pytest.raises(
        SystemExit, match="Data Validation Error: No valid data rows found"
    ):
        handle_analyze(DummyArgs())
