"""
Module for swapping the keys and values of a dictionary.
"""


def swap_keys_values(d):
    """Swaps the keys and values of a given dictionary and returns the new dictionary."""
    return {value: key for key, value in d.items()}


if __name__ == "__main__":
    original = {"a": 1, "b": 2, "c": 3}
    print(swap_keys_values(original))
