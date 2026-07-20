"""
Module for removing duplicate items from a list while preserving order.
"""


def remove_duplicates(items):
    """Removes duplicates from a list and returns a new list with the original order preserved."""
    return list(dict.fromkeys(items))


if __name__ == "__main__":
    print(remove_duplicates([3, 1, 2, 3, 2, 4, 1]))
