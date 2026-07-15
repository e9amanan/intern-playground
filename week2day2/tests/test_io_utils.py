
import pytest
import json
from insights_energy.io_utils import read_csv, write_csv, read_json, write_json
from insights_energy.exceptions import FileProcessingError, ValidationError


# CSV TESTS


def test_write_and_read_csv_success(tmp_path):
    """Happy Path: Tests if we can write a CSV and read it back correctly."""
    
    test_file = tmp_path / "test_data.csv"
    
    data_to_write = [
        {"timestamp": "2026-07-14T10:00:00", "price": "45.5"},
        {"timestamp": "2026-07-14T11:00:00", "price": "46.0"}
    ]
    
   
    write_csv(test_file, data_to_write, fieldnames=["timestamp", "price"])
    
   
    read_data = read_csv(test_file, required_column="price")
    
    assert len(read_data) == 2
    assert read_data[0]["price"] == "45.5"

def test_read_csv_missing_column(tmp_path):
    """Sad Path: Tests if ValidationError is raised when headers are wrong."""
    test_file = tmp_path / "bad_data.csv"
    
   
    write_csv(test_file, [{"timestamp": "2026-07-14", "cost": "45.5"}], fieldnames=["timestamp", "cost"])
    
   
    with pytest.raises(ValidationError) as error_info:
        read_csv(test_file, required_column="price")
        
    assert "Metric column 'price' not found" in str(error_info.value)

def test_read_csv_file_not_found():
    """Sad Path: Tests if FileProcessingError triggers for a missing file."""
    with pytest.raises(FileProcessingError):
        read_csv("does_not_exist.csv")


# JSON TESTS


def test_write_and_read_json_success(tmp_path):
    """Happy Path: Tests writing and reading valid JSON."""
    test_file = tmp_path / "test_data.json"
    
    data_to_write = [{"timestamp": "2026-07-14", "value": 45.5}]
    
    
    write_json(test_file, data_to_write)
    
    
    read_data = read_json(test_file, expected_type=list)
    
    assert len(read_data) == 1
    assert read_data[0]["value"] == 45.5

def test_read_json_invalid_structure(tmp_path):
    """Sad Path: Tests if ValidationError triggers when JSON is a dict, not a list."""
    test_file = tmp_path / "wrong_structure.json"
    
    
    bad_data = {"error": "This is not a list"}
    write_json(test_file, bad_data)
    
    with pytest.raises(ValidationError) as error_info:
        read_json(test_file, expected_type=list)
        
    assert "Expected list" in str(error_info.value)

def test_read_json_corrupted_format(tmp_path):
    """Sad Path: Tests if FileProcessingError triggers when JSON syntax is broken."""
    test_file = tmp_path / "corrupted.json"
    
    
    with open(test_file, "w") as f:
        f.write('[{"timestamp": "2026-07-14", "value": 45.5}') 
        
    with pytest.raises(FileProcessingError):
        read_json(test_file)