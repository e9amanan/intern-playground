import pytest
from unittest.mock import patch, mock_open
import sys
from week1day3.tools.csv_stats import load_csv, summarize_numeric, top_n, main

# --- 1. MOCKING TESTS ---

@patch("week1day3.tools.csv_stats.Path.is_file")
@patch("week1day3.tools.csv_stats.Path.open", new_callable=mock_open, read_data="id,price\n1,10.5\n2,20.0")
def test_load_csv_mocked(mock_file, mock_is_file):
    """
    MOCKING: We fake that the file exists, and we fake the file contents.
    The real hard drive is never touched!
    """
    mock_is_file.return_value = True
    
    result = load_csv("fake_path.csv")
    
    assert len(result) == 2
    assert result[0] == {"id": "1", "price": "10.5"}
    mock_is_file.assert_called_once_with()
    mock_file.assert_called_once_with(mode="r", encoding="utf-8")

@patch("week1day3.tools.csv_stats.Path.is_file")
def test_load_csv_file_not_found(mock_is_file):
    """Test that a FileNotFoundError is raised if the mocked system says it doesn't exist."""
    mock_is_file.return_value = False
    
    with pytest.raises(FileNotFoundError):
        load_csv("missing.csv")

@patch("sys.argv", ["csv_stats.py", "--file", "data.csv", "--metric", "price"])
@patch("week1day3.tools.csv_stats.load_csv")
def test_main_cli(mock_load_csv, capsys):
    """MOCKING"""
    mock_load_csv.return_value = [{"price": "10"}, {"price": "20"}]
    
    main()
    
    captured = capsys.readouterr()
    assert "Successfully loaded 2 rows" in captured.out
    assert "Mean: 15.00" in captured.out

# --- 2. STANDARD PURE FUNCTION TESTS ---

@pytest.fixture
def sample_rows():
    return [
        {"name": "A", "score": "80"},
        {"name": "B", "score": "90"},
        {"name": "C", "score": "invalid"}, # Should be skipped
        {"name": "D"},                     # Missing score entirely
    ]

def test_summarize_numeric(sample_rows):
    stats = summarize_numeric(sample_rows, "score")
    assert stats == {"min": 80.0, "max": 90.0, "mean": 85.0}

def test_top_n(sample_rows):
    top = top_n(sample_rows, "score", 1)
    assert len(top) == 1
    assert top[0]["name"] == "B"