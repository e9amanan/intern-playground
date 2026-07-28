import pytest
from week1day2.utils.collection_utils import frequencies, dedupe, group_by

def test_frequencies(sample_string_list):
    """Test that frequencies correctly counts items."""
    result = frequencies(sample_string_list)
    assert result == {"apple": 3, "banana": 2, "orange": 1}

@pytest.mark.parametrize("input_list, expected", [
    (["a", "b", "a"], ["a", "b"]),           # Standard case
    (["x", "x", "x"], ["x"]),                # All duplicates
    ([], []),                                # Edge case: empty list
    (["a", "b", "c"], ["a", "b", "c"]),      # No duplicates
])
def test_dedupe(input_list, expected):
    """Test deduplication with various edge cases using parametrization."""
    assert dedupe(input_list) == expected

def test_group_by(sample_dict_list):
    """Test that group_by aggregates dictionaries by a specified key."""
    grouped = group_by(sample_dict_list, "status")
    
    assert "todo" in grouped
    assert len(grouped["todo"]) == 2
    assert len(grouped["done"]) == 1
    
    assert grouped["done"][0]["id"] == 2