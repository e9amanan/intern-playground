"""
Unit tests for the advanced utility functions.
"""

import pytest
from utils.advanced import apply_to_values, chain_functions, safe_divide


# --- apply_to_values Tests ---
def test_apply_to_values_happy_path():
    """Tests that a function is correctly applied to all dictionary values."""
    data = {"apples": 2, "bananas": 5}

    result = apply_to_values(data, lambda x: x * 10)
    assert result == {"apples": 20, "bananas": 50}


def test_apply_to_values_empty_dict():
    """Tests that applying a function to an empty dictionary safely returns an empty dict."""
    assert apply_to_values({}, lambda x: x + 1) == {}


# --- safe_divide Tests ---
def test_safe_divide_happy_path():
    """Tests standard division of two valid numbers."""
    assert safe_divide(10.0, 2.0) == 5.0


def test_safe_divide_by_zero_default():
    """Tests that the default 0.0 is used when dividing by zero."""
    assert safe_divide(15.0, 0.0) == 0.0


def test_safe_divide_custom_default():
    """Tests overriding the default value on a division by zero."""
    assert safe_divide(15.0, 0.0, default=-99.9) == -99.9


def test_safe_divide_negative_numbers():
    """Tests division with negative numbers."""
    assert safe_divide(-10.0, 2.0) == -5.0


# --- chain_functions Tests ---
def test_chain_functions_happy_path():
    """Tests chaining two functions together in a pipeline."""

    # Function 1: add 5. Function 2: multiply by 2.
    def add_five(x):
        return x + 5

    def double(x):
        return x * 2

    pipeline = chain_functions(add_five, double)

    assert pipeline(10) == 30


def test_chain_functions_single_function():
    """Tests that if only one function is chained, it acts normally."""

    def make_upper(s):
        return s.upper()

    pipeline = chain_functions(make_upper)
    assert pipeline("hello") == "HELLO"


def test_chain_functions_no_functions():
    """Tests the edge case where no functions are passed; it should return the original item."""
    pipeline = chain_functions()
    assert pipeline("unchanged") == "unchanged"


# --- Error Handling Tests for advanced.py ---
def test_apply_to_values_invalid_dict():
    """Tests that passing a list instead of a dictionary crashes with an AttributeError."""
    with pytest.raises(AttributeError):
        apply_to_values(["a", "b", "c"], lambda x: x * 2)


def test_apply_to_values_invalid_function():
    """Tests that passing a non-callable instead of a function throws a TypeError."""
    data = {"apples": 2}
    with pytest.raises(TypeError):
        apply_to_values(data, 123)


def test_safe_divide_string_input():
    """Tests that passing string inputs to safe_divide throws a TypeError."""
    with pytest.raises(TypeError):
        safe_divide("10", "2")
