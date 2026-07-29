import pytest
from week1weekend.dictionary.characterfrq import char_frequency

@pytest.mark.parametrize("input_str, expected", [
    ("hello", {"h": 1, "e": 1, "l": 2, "o": 1}),
    ("", {}),
    ("aaa", {"a": 3}),
])
def test_char_frequency(input_str, expected):
    """Test character frequencies in strings."""
    assert char_frequency(input_str) == expected