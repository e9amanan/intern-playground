from week1weekend.dictionary.wordlength import word_lengths

def test_word_lengths():
    """Test calculating lengths of words in a list."""
    words = ["apple", "banana", "cherry"]
    expected = {"apple": 5, "banana": 6, "cherry": 6}
    
    assert word_lengths(words) == expected
    assert word_lengths([]) == {}