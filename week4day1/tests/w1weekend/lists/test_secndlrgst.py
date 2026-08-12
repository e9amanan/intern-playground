import pytest

from week1weekend.lists.secndlrgst import second_largest


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([10, 20, 4, 45, 99, 99, 45], 45),
        ([10, 10, 10], None),
        ([5], None),
        ([-5, -10, -2, -1], -2),
    ],
)
def test_second_largest(nums, expected):
    """Test finding the second largest unique number."""
    assert second_largest(nums) == expected
