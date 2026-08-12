import pytest

from week1weekend.lists.subarrayindex import subarray_sum


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 2, 3, 7, 5], 12, [2, 4]),
        ([1, 2, 3, 4, 5], 9, [2, 4]),
        ([1, 2, 3], 10, [-1]),
        ([5], 5, [1, 1]),
    ],
)
def test_subarray_sum(arr, target, expected):
    """Test finding contiguous subarray sums."""
    assert subarray_sum(arr, target) == expected
