import pytest
from week1day3.controlflows.tryexcept import calculatingaverage

def test_calculatingaverage_valid(capsys):
    result = calculatingaverage([10, 20, 30])
    captured = capsys.readouterr()
    
    assert result == 20.0
    assert "calculation succesful" in captured.out
    assert "executionfinished" in captured.out

def test_calculatingaverage_empty(capsys):
    result = calculatingaverage([])
    captured = capsys.readouterr()
    
    assert result is None
    assert "validation error:cannot calculate average of empty list" in captured.out

def test_calculatingaverage_type_error(capsys):
    result = calculatingaverage([10, "string", 30])
    captured = capsys.readouterr()
    
    assert result is None
    assert "error:list contains non numeric values" in captured.out