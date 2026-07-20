"""
Module for finding the smallest multiple evenly divisible by all numbers in a range.
"""
import math


def compute_lcm(a, b):
    """Calculates the Least Common Multiple (LCM) of two integers."""
    return (a * b) // math.gcd(a, b)


def find_smallest_multiple(limit):
    """
    Finds the smallest positive number that is evenly divisible by all 
    numbers from 1 up to the given limit.
    """
    smallest_multiple = 1
    for i in range(1, limit + 1):
        smallest_multiple = compute_lcm(smallest_multiple, i)
    return smallest_multiple


if __name__ == "__main__":
    # We want to find the smallest multiple for numbers 1 through 20
    RESULT = find_smallest_multiple(20)
    print(RESULT)