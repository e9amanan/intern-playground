import json
from unittest.mock import mock_open, patch

import pytest

from week2day2.insights_energy.exceptions import FileProcessingError, ValidationError
from week2day2.insights_energy.io_utils import (
    read_csv,
    read_json,
    write_csv,
    write_json,
)

# --- CSV Tests ---


@patch("week2day2.insights_energy.io_utils.Path.exists")
def test_read_csv_missing_file(mock_exists):
    mock_exists.return_value = False
    with pytest.raises(FileProcessingError, match="does not exist"):
        read_csv("missing.csv", "price")


@patch("week2day2.insights_energy.io_utils.Path.is_file")
@patch("week2day2.insights_energy.io_utils.Path.exists")
@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="timestamp,price\n2023-01-01,50.0",
)
def test_read_csv_success(mock_file, mock_exists, mock_is_file):
    mock_exists.return_value = True
    mock_is_file.return_value = True

    data = read_csv("valid.csv", "price")

    assert len(data) == 1
    assert data[0]["price"] == "50.0"


@patch("week2day2.insights_energy.io_utils.Path.is_file")
@patch("week2day2.insights_energy.io_utils.Path.exists")
@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="timestamp,wrong_col\n2023-01-01,50.0",
)
def test_read_csv_missing_column(mock_file, mock_exists, mock_is_file):
    mock_exists.return_value = True
    mock_is_file.return_value = True

    with pytest.raises(ValidationError, match="Metric column 'price' not found"):
        read_csv("bad_headers.csv", "price")


@patch("builtins.open", new_callable=mock_open)
def test_write_csv(mock_file):
    data = [{"timestamp": "2023-01-01", "value": 50.0}]
    write_csv("out.csv", data, ["timestamp", "value"])
    mock_file.assert_called_once_with("out.csv", mode="w", encoding="utf-8", newline="")


# --- JSON Tests ---


@patch("week2day2.insights_energy.io_utils.Path.exists")
@patch("builtins.open", new_callable=mock_open, read_data='[{"value": 10}]')
def test_read_json_success(mock_file, mock_exists):
    mock_exists.return_value = True

    data = read_json("data.json", expected_type=list)
    assert isinstance(data, list)
    assert data[0]["value"] == 10


@patch("week2day2.insights_energy.io_utils.Path.exists")
@patch("builtins.open", new_callable=mock_open, read_data='{"value": 10}')
def test_read_json_type_validation_error(mock_file, mock_exists):
    mock_exists.return_value = True

    with pytest.raises(ValidationError, match="Expected data type list, but got dict"):
        read_json("data.json", expected_type=list)


@patch("builtins.open", new_callable=mock_open)
def test_write_json(mock_file):
    write_json("out.json", [{"test": 1}])
    mock_file.assert_called_once_with("out.json", mode="w", encoding="utf-8")
