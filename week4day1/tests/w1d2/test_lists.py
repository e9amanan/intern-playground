import pytest

from week1day2.pythonexercises.lists import (
    chunk_list,
    flatten_simple,
    merge_sorted_simple,
)


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([], [1, 2], [1, 2]),
        ([5, 5], [5], [5, 5, 5]),
    ],
)
def test_merge_sorted_simple(list1, list2, expected):
    """Test merging two lists and sorting them."""
    assert merge_sorted_simple(list1, list2) == expected


def test_chunk_list():
    """Test splitting a list into sized chunks."""
    items = [1, 2, 3, 4, 5]
    assert chunk_list(items, 2) == [[1, 2], [3, 4], [5]]
    assert chunk_list(items, 5) == [[1, 2, 3, 4, 5]]


def test_flatten_simple():
    """Test flattening a nested list."""
    nested = [[1, 2], [3, 4], [5]]
    assert flatten_simple(nested) == [1, 2, 3, 4, 5]
