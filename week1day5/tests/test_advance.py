import pytest
from utils.advanced import apply_to_values, safe_divide, chain_functions

# --- apply_to_values Tests ---
def test_apply_to_values_happy_path():
    data = {"apples": 2, "bananas": 5}
    # Multiply all values by 10
    result = apply_to_values(data, lambda x: x * 10)
    assert result == {"apples": 20, "bananas": 50}

def test_apply_to_values_empty_dict():
    # Running it on an empty dictionary should safely return an empty dictionary
    assert apply_to_values({}, lambda x: x + 1) == {}

# --- safe_divide Tests ---
def test_safe_divide_happy_path():
    assert safe_divide(10.0, 2.0) == 5.0

def test_safe_divide_by_zero_default():
    # Tests that the default 0.0 is used when dividing by zero
    assert safe_divide(15.0, 0.0) == 0.0

def test_safe_divide_custom_default():
    # Tests overriding the default value
    assert safe_divide(15.0, 0.0, default=-99.9) == -99.9

def test_safe_divide_negative_numbers():
    assert safe_divide(-10.0, 2.0) == -5.0

# --- chain_functions Tests ---
def test_chain_functions_happy_path():
    # Function 1: add 5. Function 2: multiply by 2.
    add_five = lambda x: x + 5
    double = lambda x: x * 2
    
    # Create the pipeline
    pipeline = chain_functions(add_five, double)
    
    # Process: (10 + 5) * 2 = 30
    assert pipeline(10) == 30

def test_chain_functions_single_function():
    # If only one function is chained, it should act normally
    make_upper = lambda s: s.upper()
    pipeline = chain_functions(make_upper)
    
    assert pipeline("hello") == "HELLO"

def test_chain_functions_no_functions():
    # Edge case: If no functions are passed, it should just return the original item
    pipeline = chain_functions()
    assert pipeline("unchanged") == "unchanged"

# --- Error Handling Tests for advanced.py ---

def test_apply_to_values_invalid_dict():
    # apply_to_values relies on 'd.items()'.
    # If we pass a list instead of a dictionary, it crashes because lists don't have .items().
    with pytest.raises(AttributeError):
        apply_to_values(["a", "b", "c"], lambda x: x * 2)

def test_apply_to_values_invalid_function():
    # If we pass a random number instead of an actual function, 
    # the code `func(value)` will try to run `123(value)`, which throws a TypeError.
    data = {"apples": 2}
    with pytest.raises(TypeError):
        apply_to_values(data, 123)

def test_safe_divide_string_input():
    # safe_divide uses the '/' operator.
    # If we accidentally pass strings from a text file, Python cannot divide them.
    with pytest.raises(TypeError):
        safe_divide("10", "2")