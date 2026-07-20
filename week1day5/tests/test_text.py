"""
Unit tests for the text utility functions in week1day2.
"""

import pytest

from week1day2.utils.text import clean_text, count_chars, tokenize


def test_clean_text_happy_path():
    """Tests that text is converted to lowercase and stripped of extra spaces."""
    assert clean_text(" HEllo, WORLd!  ") == "hello, world!"


def test_clean_text_edge_cases():
    """Tests clean_text with empty strings, blank spaces, and multiple inner spaces."""
    assert clean_text("") == ""
    assert clean_text("    ") == ""
    assert clean_text("HEllo  woRLd      HoW") == "hello world how"


def test_tokenize_custom_delimiter():
    """Tests that tokenize correctly splits a string using a custom delimiter."""
    assert tokenize("apple,banana,orange", delimiter=",") == [
        "apple",
        "banana",
        "orange",
    ]


def test_tokenize_happy_path():
    """Tests that tokenize correctly splits a string by default whitespace."""
    assert tokenize("hello world") == ["hello", "world"]


def test_tokenize_edge_case():
    """Tests tokenize with an empty string."""
    assert tokenize("") == [""]


def test_count_chars_happy_path():
    """Tests that character frequencies are correctly counted."""
    assert count_chars("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}


def test_count_chars_edge_case():
    """Tests that an empty string returns an empty dictionary (using implicit boolean evaluation)"""
    assert not count_chars("")


def test_tokenize_edge_case1():
    """Tests tokenize on a string without the custom delimiter present."""
    assert tokenize("123", delimiter=",") == ["123"]


def test_tokenize_invalid_type_integer():
    """Tests that passing an integer to tokenize raises an AttributeError."""
    with pytest.raises(AttributeError):
        tokenize(123)


def test_tokenize_invalid_type_none():
    """Tests that passing None to tokenize raises an AttributeError."""
    with pytest.raises(AttributeError):
        tokenize(None)
