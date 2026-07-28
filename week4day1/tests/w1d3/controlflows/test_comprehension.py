from week1day3.controlflows.comprehension import valid_prices, clean_header, unique_tags

def test_comprehension_results():
    """Test that the comprehensions accurately filtered and transformed the data."""
    assert valid_prices == [12.5, 95.2, 45.0]
    assert clean_header == {0: "user_id", 1: "email@test.com", 2: "status"}
    assert unique_tags == {"python", "java", "c++"}