import pytest
from unittest.mock import patch, mock_open
from week2day5.yourpkg.cli import main, handle_analyze, _load_csv
from week2day5.yourpkg.exception import FileProcessingError, ValidationError


# --- Testing _load_csv helper ---

@patch("builtins.open", new_callable=mock_open, read_data="timestamp,price\n2023-10-01,50.0")
def test_load_csv_success(mock_file):
    result = _load_csv("dummy.csv")
    assert len(result) == 1
    assert result[0]["price"] == "50.0"


@patch("builtins.open")
def test_load_csv_file_not_found(mock_file):
    mock_file.side_effect = FileNotFoundError
    with pytest.raises(FileProcessingError, match="was not found"):
        _load_csv("missing.csv")


@patch("builtins.open")
def test_load_csv_generic_error(mock_file):
    mock_file.side_effect = PermissionError("Access denied")
    with pytest.raises(FileProcessingError, match="Failed to read file"):
        _load_csv("locked.csv")


# --- Testing handle_analyze ---

@patch("week2day5.yourpkg.cli._load_csv")
@patch("week2day5.yourpkg.core.clean_data")
def test_handle_analyze_success(mock_clean, mock_load, capsys):
    # Setup mocks
    mock_load.return_value = []
    mock_clean.return_value = [{"raw_ts": "t1", "timestamp": "t1", "value": 10.0}]
    
    class DummyArgs:
        file = "dummy.csv"
        metric = "price"
        top = 3
        
    exit_code = handle_analyze(DummyArgs())
    
    assert exit_code == 0
    captured = capsys.readouterr()
    assert "Daily averages:" in captured.out


@patch("week2day5.yourpkg.cli._load_csv")
def test_handle_analyze_file_error(mock_load):
    mock_load.side_effect = FileProcessingError("Bad file")
    
    class DummyArgs:
        file = "dummy.csv"
        metric = "price"
        top = 3
        
    with pytest.raises(SystemExit, match="File Error: Bad file"):
        handle_analyze(DummyArgs())


@patch("week2day5.yourpkg.cli._load_csv")
@patch("week2day5.yourpkg.core.clean_data")
def test_handle_analyze_validation_error(mock_clean, mock_load):
    mock_load.return_value = []
    mock_clean.side_effect = ValidationError("Bad data")
    
    class DummyArgs:
        file = "dummy.csv"
        metric = "price"
        top = 3
        
    with pytest.raises(SystemExit, match="Data Validation Error: Bad data"):
        handle_analyze(DummyArgs())


# --- Testing main ---

@patch("week2day5.yourpkg.cli.handle_analyze")
def test_main_arg_parsing(mock_handle):
    mock_handle.return_value = 0
    test_args = ["analyze", "-f", "test.csv", "-m", "cost", "-t", "5"]
    
    exit_code = main(test_args)
    
    assert exit_code == 0
    # Verify the arguments were correctly parsed and passed to the handler
    args_passed = mock_handle.call_args[0][0]
    assert args_passed.file == "test.csv"
    assert args_passed.metric == "cost"
    assert args_passed.top == 5