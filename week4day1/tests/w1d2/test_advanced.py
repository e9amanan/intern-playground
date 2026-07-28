import pytest

from week1day2.utils.advanced import apply_to_values, chain_functions, safe_divide


def test_apply_to_values(sample_number_dict):
    """Test applying a lambda function to all dictionary values."""
    result = apply_to_values(sample_number_dict, lambda x: x * 2)
    assert result == {"a": 20, "b": 40, "c": 60}


@pytest.mark.parametrize(
    "a, b, default, expected",
    [
        (10.0, 2.0, 0.0, 5.0),  # Normal division
        (10.0, 0.0, 0.0, 0.0),  # Division by zero (returns default 0.0)
        (10.0, 0.0, -1.0, -1.0),  # Division by zero (returns custom default -1.0)
        (0.0, 5.0, 0.0, 0.0),  # Zero divided by a number
    ],
)
def test_safe_divide(a, b, default, expected):
    """Test safe division including zero denominator scenarios."""
    assert safe_divide(a, b, default) == expected


def test_chain_functions():
    """Test chaining string methods together."""
    func = chain_functions(str.strip, str.lower, str.title)
    assert func("  hElLo wOrLd  ") == "Hello World"
