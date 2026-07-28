import pytest

from week1day2.pythonexercises.strings import (
    is_palindrome,
    reverse_words,
    title_case_simple,
)


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("racecar", True),
        ("A man a plan a canal Panama", True),  # Tests spaces and caps
        ("hello", False),
        ("", True),
    ],
)
def test_is_palindrome(input_str, expected):
    """Test palindrome logic with various edge cases."""
    assert is_palindrome(input_str) == expected


def test_reverse_words():
    """Test reversing the order of words in a string."""
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("one two three") == "three two one"


def test_title_case_simple():
    """Test title casing strings."""
    assert title_case_simple("hello world") == "Hello World"
