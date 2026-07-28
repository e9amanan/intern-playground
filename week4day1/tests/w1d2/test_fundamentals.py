from week1day2.fundamentals import (
    CLEAN,
    DOUBLES,
    EVENS,
    FULLSTACK,
    SQUARES,
    TEXT,
    WORDS,
    Color,
)


def test_string_operations():
    """Verify the script correctly sliced and cleaned strings."""
    assert TEXT == "python"
    assert WORDS == ["lets", "learn", "python", "today"]
    assert CLEAN == "hello world  how are you"


def test_list_comprehensions():
    """Verify the list comprehensions calculated the right math."""
    assert DOUBLES == [2, 4, 6, 8, 10]
    assert EVENS == [4, 8]


def test_namedtuple():
    """Verify the Color namedtuple was structured properly."""
    pure_red = Color(red=255, green=0, blue=0)
    assert pure_red.red == 255


def test_dictionary_comprehension():
    """Verify dictionary comprehension mapped numbers to squares."""
    assert SQUARES == {1: 1, 2: 4, 3: 9, 4: 16}


def test_set_operations():
    """Verify set intersections logic (Frontend & Backend)."""
    assert FULLSTACK == {"Charlie"}
