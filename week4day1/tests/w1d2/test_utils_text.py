import pytest

from week1day2.utils.text import clean_text, tokenize, count_chars

@pytest.mark.parametrize("input_str, expected", [
    (" Hello, WORLD! ", "hello, world!"),
    ("multiple   spaces", "multiple spaces"),
    ("", ""),
    ("  already lowercase  ", "already lowercase"),
])
def test_clean_text_basic(input_str, expected):
    """Basic example-based testing for clean_text."""
    assert clean_text(input_str) == expected

def test_clean_text_manual_idempotence():
    """
    Manually testing idempotence without the hypothesis library.
    Running the function twice should equal running it once.
    """
    first_pass = clean_text("  Make ME   clean!  ")
    second_pass = clean_text(first_pass)
    
    assert first_pass == "make me clean!"
    assert second_pass == "make me clean!"
    assert first_pass == second_pass

def test_tokenize():
    """Test string tokenization with default and custom delimiters."""
    assert tokenize("hello, world!") == ["hello,", "world!"]
    assert tokenize("a|b|c", delimiter="|") == ["a", "b", "c"]
    assert tokenize("") == [""]

def test_count_chars():
    """Test character frequency counter."""
    assert count_chars("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
    assert count_chars("") == {}