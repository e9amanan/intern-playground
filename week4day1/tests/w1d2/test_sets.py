from week1day2.pythonexercises.sets import common_elements, unique_chars, is_subset

def test_common_elements():
    """Test finding intersections between two lists."""
    assert common_elements([1, 2, 3], [2, 3, 4]) == {2, 3}
    assert common_elements([1, 2], [3, 4]) == set()

def test_unique_chars():
    """Test string to set conversion."""
    assert unique_chars("hello") == {"h", "e", "l", "o"}

def test_is_subset():
    """Test subset boolean logic."""
    assert is_subset({1, 2}, {1, 2, 3}) == True
    assert is_subset({1, 4}, {1, 2, 3}) == False