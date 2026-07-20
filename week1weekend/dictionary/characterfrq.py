"""
Module for calculating character frequencies within a string.
"""

from collections import Counter


def char_frequency(s):
    """Returns a dictionary containing the frequency of each character in the input string."""
    return dict(Counter(s))
