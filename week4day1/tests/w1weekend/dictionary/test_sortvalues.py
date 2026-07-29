from week1weekend.dictionary.sortvalues import sort_by_values

def test_sort_by_values():
    """Test sorting dictionaries by values in descending order."""
    data = {"a": 10, "b": 50, "c": 30}
    expected = [("b", 50), ("c", 30), ("a", 10)]
    
    assert sort_by_values(data) == expected
    assert sort_by_values({}) == []