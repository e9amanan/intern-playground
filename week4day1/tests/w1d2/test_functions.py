import pytest

from week1day2.functions import (
    power, 
    get_min_max, 
    greet, 
    create_profile
)

@pytest.mark.parametrize("base, exponent, expected", [
    (3, 3, 27),
    (2, 4, 16),
    (5, 2, 25),  # Testing default behavior
])
def test_power(base, exponent, expected):
    """Test the power function with and without default arguments."""
    assert power(base, exponent) == expected

def test_get_min_max():
    """Test that it correctly identifies the lowest and highest numbers."""
    assert get_min_max([10, 20, 5, 40]) == (5, 40)
    assert get_min_max([7, 7, 7]) == (7, 7)

def test_greet():
    """Test the type-hinted greeting function."""
    assert greet("Alice", 25) == "Hello Alice, you are 25 years old."

def test_create_profile_prints(capsys):
    """
    Test a function that prints instead of returning using the capsys fixture.
    """
    create_profile("Alice", 25, "Engineer", location="NYC", active=True)
    captured = capsys.readouterr()
    
    assert "Name: Alice" in captured.out
    assert "Extra positional args: (25, 'Engineer')" in captured.out
    assert "'location': 'NYC'" in captured.out