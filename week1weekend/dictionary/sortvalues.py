"""
Module for sorting dictionaries by their values.
"""


def sort_by_values(d):
    """Sorts a dictionary by its values in descending order."""
    return sorted(d.items(), key=lambda item: item[1], reverse=True)


if __name__ == "__main__":
    data = {"a": 10, "b": 50, "c": 30}
    print(sort_by_values(data))
