import pytest
from unittest.mock import patch
from week2day2.insights_energy.__main__ import validate_top_argument, main

# --- Validation Tests ---

@pytest.mark.parametrize("top_n", [1, 5, 10, 100])
def test_validate_top_argument_valid(top_n):
    """Test valid positive integers pass silently."""
    validate_top_argument(top_n)

@pytest.mark.parametrize("invalid_top", [0, -5])
def test_validate_top_argument_invalid_value(invalid_top):
    with pytest.raises(ValueError, match="positive integer"):
        validate_top_argument(invalid_top)

@pytest.mark.parametrize("invalid_type", ["10", 10.5, None])
def test_validate_top_argument_invalid_type(invalid_type):
    with pytest.raises(TypeError, match="must be an integer"):
        validate_top_argument(invalid_type)

# --- CLI Flow Tests ---

@patch("sys.argv", ["__main__.py", "--file", "test.csv"])
@patch("week2day2.insights_energy.__main__.read_csv")
@patch("week2day2.insights_energy.__main__.clean_data")
def test_main_success_flow(mock_clean, mock_read, capsys):
    mock_read.return_value = []
    mock_clean.return_value = [{"raw_ts": "t1", "timestamp": "t1", "value": 10.0}] * 3
    
    main()
    
    captured = capsys.readouterr()
    assert "Daily averages:" in captured.out
    assert "Top 10 price spikes:" in captured.out

@patch("sys.argv", ["__main__.py", "--file", "test.csv", "--export", "json"])
@patch("week2day2.insights_energy.__main__.read_csv")
@patch("week2day2.insights_energy.__main__.clean_data")
@patch("week2day2.insights_energy.__main__.write_json")
def test_main_export_json(mock_write_json, mock_clean, mock_read, capsys):
    mock_read.return_value = []
    mock_clean.return_value = [{"raw_ts": "t1", "timestamp": "t1", "value": 10.0}]
    
    main()
    
    captured = capsys.readouterr()
    assert "Data successfully exported to cleaned_data.json" in captured.out
    mock_write_json.assert_called_once()