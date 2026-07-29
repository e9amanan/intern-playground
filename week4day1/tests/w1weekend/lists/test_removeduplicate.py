from week1weekend.lists.removeduplicate import remove_duplicates

def test_remove_duplicates():
    """Test removing duplicates while maintaining insertion order."""
    assert remove_duplicates([3, 1, 2, 3, 2, 4, 1]) == [3, 1, 2, 4]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([]) == []