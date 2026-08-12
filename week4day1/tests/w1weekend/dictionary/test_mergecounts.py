from week1weekend.dictionary.mergecounts import merge_inventories


def test_merge_inventories():
    """Test merging and summing inventory dictionaries."""
    inv_a = {"apples": 10, "bananas": 5}
    inv_b = {"bananas": 12, "oranges": 8}
    expected = {"apples": 10, "bananas": 17, "oranges": 8}

    assert merge_inventories(inv_a, inv_b) == expected
    assert merge_inventories({}, {}) == {}
