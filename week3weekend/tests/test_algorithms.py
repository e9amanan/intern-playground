import pytest
from algorithms.search import binary_search_iterative
from algorithms.sort import merge_sort, quick_sort
from algorithms.tree_traversal import Node, bfs_level_order, dfs_iterative


# --- SEARCH TESTS ---
@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 2, 3, 4, 5], 3, 2),  # Happy path
        ([1, 2, 3, 4, 5], 6, -1),  # Not found
        ([], 5, -1),  # Edge: Empty list
        ([1], 1, 0),  # Edge: Single element
        ([-5, -2, 0, 3, 9], -2, 1),  # Edge: Negative numbers
    ],
)
def test_binary_search_iterative(arr, target, expected):
    assert binary_search_iterative(arr, target) == expected


# --- SORT TESTS ---
@pytest.mark.parametrize(
    "arr, expected",
    [
        ([3, 1, 4, 1, 5], [1, 1, 3, 4, 5]),  # Happy path with duplicates
        ([], []),  # Edge: Empty list
        ([1], [1]),  # Edge: Single element
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Edge: Reverse sorted
    ],
)
def test_merge_sort(arr, expected):
    assert merge_sort(arr) == expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([3, 1, 4, 1, 5], [1, 1, 3, 4, 5]),
        ([], []),
        ([1], [1]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([-5, 0, -10, 5], [-10, -5, 0, 5]),
    ],
)
def test_quick_sort(arr, expected):
    assert quick_sort(arr) == expected


# --- TRAVERSAL TESTS ---
def test_bfs_level_order():
    # Tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = Node(1)
    root.left = Node(2, Node(4), Node(5))
    root.right = Node(3)

    assert bfs_level_order(root) == [[1], [2, 3], [4, 5]]
    assert bfs_level_order(None) == []


def test_dfs_iterative():
    root = Node(1)
    root.left = Node(2, Node(4), Node(5))
    root.right = Node(3)

    # Preorder DFS: 1 -> 2 -> 4 -> 5 -> 3
    assert dfs_iterative(root) == [1, 2, 4, 5, 3]
