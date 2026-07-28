from unittest.mock import patch

from week1day3.controlflows.contextmanager import TimerContext


@patch("week1day3.controlflows.contextmanager.time.time")
def test_timer_context(mock_time, capsys):
    """
    MOCKING
    """
    mock_time.side_effect = [100.0, 102.0]

    with TimerContext():
        pass

    captured = capsys.readouterr()
    assert "Timer started..." in captured.out
    assert "Block took 2.0000 seconds" in captured.out
