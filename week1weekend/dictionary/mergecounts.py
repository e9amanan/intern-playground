"""
Module for merging and calculating total inventory counts.
"""

from collections import Counter


def merge_inventories(inv1, inv2):
    """Merges two inventory dictionaries, summing the counts of matching items."""
    return dict(Counter(inv1) + Counter(inv2))


if __name__ == "__main__":
    inv_a = {"apples": 10, "bananas": 5}
    inv_b = {"bananas": 12, "oranges": 8}
    print(merge_inventories(inv_a, inv_b))
