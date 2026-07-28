import pytest
from week1day3.controlflows.leetcode.product_except_self import product_except_self
from week1day3.controlflows.leetcode.valid_paranthesis import is_valid

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ([0, 0], [0, 0]),
])
def test_product_except_self(nums, expected):
    assert product_except_self(nums) == expected

@pytest.mark.parametrize("s, expected", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("]", False),  # Edge case: starts with closing bracket
    ("", True),    # Edge case: empty string
])
def test_is_valid_parenthesis(s, expected):
    assert is_valid(s) == expected