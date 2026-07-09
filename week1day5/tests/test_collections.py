import pytest

from utils.collection_utils import frequencies, deduce, group_by


def test_frequencies_happy_path():
    assert frequencies(["a", "b", "a", "c"]) == {"a": 2, "b": 1, "c": 1}

def test_frequencies_empty_list():
                                          # An empty list
    assert frequencies([]) == {}

def test_frequencies_single_item():
    assert frequencies(["apple"]) == {"apple": 1}


def test_deduce_happy_path():
                                                 # Tests that duplicates are removed 
    assert deduce(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]

def test_deduce_no_duplicates():
                                                    # If there are no duplicates,
    assert deduce(["x", "y", "z"]) == ["x", "y", "z"]

def test_deduce_empty_list():
    assert deduce([]) == []


def test_group_by_happy_path():
    data = [
        {"role": "admin", "name": "Alice"},
        {"role": "user", "name": "Bob"},
        {"role": "admin", "name": "Charlie"}
    ]
    expected = {
        "admin": [{"role": "admin", "name": "Alice"}, {"role": "admin", "name": "Charlie"}],
        "user": [{"role": "user", "name": "Bob"}]
    }
    assert group_by(data, "role") == expected

def test_group_by_missing_key():
                                                  # If the key doesn't exist in a dictionary
    
    data = [
        {"name": "Alice"},
        {"role": "admin", "name": "Charlie"}
    ]
    expected = {
        None: [{"name": "Alice"}],
        "admin": [{"role": "admin", "name": "Charlie"}]
    }
    assert group_by(data, "role") == expected



def test_frequencies_invalid_type():
                                            # If we pass an integer (123) instead of a list
     with pytest.raises(TypeError):
        frequencies(123)

def test_deduce_unhashable_type():
    
                                             # Dictionaries are strict: you CANNOT use a list as a dictionary key. 
                                             # If we pass a list of lists,
    with pytest.raises(TypeError):
        deduce([["apple"], ["banana"]])

def test_group_by_invalid_data_type():
    
                                              # If we pass a list of strings, the line `item.get(key)` will crash,
                                              # because strings do not have a .get() method.
    with pytest.raises(AttributeError):
        group_by(["just", "random", "strings"], "status")