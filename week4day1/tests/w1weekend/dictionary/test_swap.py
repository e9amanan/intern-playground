from week1weekend.dictionary.swap import swap_keys_values

def test_swap_keys_values():
    """Test swapping keys and values in a dictionary."""
    original = {"a": 1, "b": 2, "c": 3}
    expected = {1: "a", 2: "b", 3: "c"}
    
    assert swap_keys_values(original) == expected
    assert swap_keys_values({}) == {}