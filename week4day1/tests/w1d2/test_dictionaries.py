from week1day2.pythonexercises.dictionaries import invert_dict, merge_dicts


def test_invert_dict():
    """Test that keys and values are swapped."""
    assert invert_dict({"a": "1", "b": "2"}) == {"1": "a", "2": "b"}
    assert invert_dict({}) == {}


def test_merge_dicts():
    """Test merging multiple dictionaries with overwriting."""
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}  # 'b' should overwrite dict1's 'b'
    dict3 = {"d": 5}

    assert merge_dicts(dict1, dict2, dict3) == {"a": 1, "b": 3, "c": 4, "d": 5}
