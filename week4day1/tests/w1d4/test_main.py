import sys
from unittest.mock import mock_open, patch

import pytest

from week1day4.energy_insights.__main__ import main


@patch("sys.argv", ["__main__.py", "fake_data.csv"])
@patch(
    "builtins.open", new_callable=mock_open, read_data="col1,col2\nval1,val2\nval3,val4"
)
def test_main_success(mock_file, capsys):
    "test a successful CLI run"

    main()
    captured = capsys.readouterr()

    assert "Loaded 2 rows. " in captured.out
    mock_file.assert_called_once_with("fake_data.csv", mode="r", encoding="utf-8")


@patch("sys.argv", ["__main__.py", "missing.csv"])
@patch("builtins.open")
def test_main_file_not_found(mock_file, capsys):
    "testing the program exit"

    mock_file.side_effect = FileNotFoundError

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1

    captured = capsys.readouterr()
    assert "error:file 'missing.csv' not found" in captured.out
