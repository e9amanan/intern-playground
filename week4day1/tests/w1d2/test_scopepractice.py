import pytest

from week1day2.pythonexercises.scopepractice import increment, outer


def test_increment_raises_error():
    """
    Test that modifying a global variable without the 'global' keyword
    properly raises an UnboundLocalError as expected in the comments.
    """
    with pytest.raises(UnboundLocalError):
        increment()


def test_outer():
    """Test LEGB rule where inner scope overrides enclosing scope."""
    assert outer() == "inner"
