import pytest
import importlib

def test_loops_script_output(capsys):
    """
    Since loops.py runs immediately on import, we can force an import
    inside the test and capture everything it prints to the terminal.
    """
    # Import the module to trigger the loops
    from week1day3.controlflows import loops
    
    # Reload it just in case another test already imported it
    importlib.reload(loops)
    
    captured = capsys.readouterr()
    
    # Asserting the for/else loop logic
    assert "record not found" in captured.out
    
    # Asserting the while loop truthy/falsy logic
    assert "Processing valid item: 1" in captured.out
    assert "Skipping falsy item at index 2" in captured.out # The 0
    assert "Skipping falsy item at index 4" in captured.out # The None