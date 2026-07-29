import pytest
from week2day1.task_project.examples.usage import main

def test_usage_script_output(capsys):
    """Test that the usage script creates tasks, advances status, and prints correctly."""
    main()

    captured = capsys.readouterr()
    
    assert "pending tasks(2):" in captured.out
    assert "- Complete OOP Exercise [in_progress]" in captured.out
    assert "- review Leetcode [in_progress]" in captured.out