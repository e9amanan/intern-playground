"""
Module for flattening nested lists into a single one-dimensional list.
"""


def flatten_list(nested_list):
    """Flattens a list of lists into a single list containing all elements."""
    return [item for sublist in nested_list for item in sublist]


if __name__ == "__main__":
    print(flatten_list([[1, 2], [3, 4, 5], [6]]))