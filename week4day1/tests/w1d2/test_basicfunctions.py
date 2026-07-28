import pytest

from week1day2.pythonexercises.basicfunctions import (
    calculate_stats,
    calculate_stats_numpy,
    greet,
)


def test_greet():
    """Test greeting with and without default arguments."""
    assert greet("Alice") == "Hello,Alice"
    assert greet("Bob", "Hi") == "Hi,Bob"


def test_calculate_stats():
    """Test standard math statistics."""
    result = calculate_stats(1.0, 2.0, 3.0, 4.0, 5.0)
    assert result == {"min": 1.0, "max": 5.0, "mean": 3.0, "median": 3.0}


def test_calculate_stats_numpy():
    """Test numpy statistics implementation."""
    result = calculate_stats_numpy(1.0, 2.0, 3.0, 4.0, 5.0)
    assert result == {"min": 1.0, "max": 5.0, "mean": 3.0, "median": 3.0}
