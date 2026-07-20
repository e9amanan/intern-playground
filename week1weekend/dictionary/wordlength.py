"""
Module for calculating the lengths of words in a list.
"""


def word_lengths(words):
    """Returns a dictionary mapping each word to its character length."""
    return {word: len(word) for word in words}


if __name__ == "__main__":
    print(word_lengths(["apple", "banana", "cherry"]))