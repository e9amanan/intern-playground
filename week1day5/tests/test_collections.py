"""
Unit tests for the collection_utils module.
"""

import pytest
from week1day2.utils.collection_utils import deduce, frequencies, group_by


def test_frequencies_happy_path():
    """Tests standard frequency counting of items in a list."""
    assert frequencies(["a", "b", "a", "c"]) == {"a": 2, "b": 1, "c": 1}


def test_frequencies_empty_list():
    """Tests that an empty list returns an empty dictionary."""
    assert frequencies([]) == {}


def test_frequencies_single_item():
    """Tests frequency counting with a single item in the list."""
    assert frequencies(["apple"]) == {"apple": 1}


def test_deduce_happy_path():
    """Tests that duplicates are correctly removed from a list."""
    assert deduce(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]


def test_deduce_no_duplicates():
    """Tests that deduce leaves a list without duplicates unchanged."""
    assert deduce(["x", "y", "z"]) == ["x", "y", "z"]


def test_deduce_empty_list():
    """Tests that an empty list safely returns an empty list."""
    assert deduce([]) == []


def test_group_by_happy_path():
    """Tests grouping a list of dictionaries by a specific key."""
    data = [
        {"role": "admin", "name": "Alice"},
        {"role": "user", "name": "Bob"},
        {"role": "admin", "name": "Charlie"},
    ]
    expected = {
        "admin": [
            {"role": "admin", "name": "Alice"},
            {"role": "admin", "name": "Charlie"},
        ],
        "user": [{"role": "user", "name": "Bob"}],
    }
    assert group_by(data, "role") == expected


def test_group_by_missing_key():
    """Tests group_by when a dictionary is missing the target key (groups under None)."""
    data = [{"name": "Alice"}, {"role": "admin", "name": "Charlie"}]
    expected = {
        None: [{"name": "Alice"}],
        "admin": [{"role": "admin", "name": "Charlie"}],
    }
    assert group_by(data, "role") == expected


def test_frequencies_invalid_type():
    """Tests that frequencies raises a TypeError if an integer is passed instead of an iterable."""
    with pytest.raises(TypeError):
        frequencies(123)


def test_deduce_unhashable_type():
    """Tests that deduce raises a TypeError for unhashable types (like lists of lists)."""
    with pytest.raises(TypeError):
        deduce([["apple"], ["banana"]])


def test_group_by_invalid_data_type():
    """Tests that group_by raises an AttributeError if strings are passed instead of dicts."""
    with pytest.raises(AttributeError):
        group_by(["just", "random", "strings"], "status")
