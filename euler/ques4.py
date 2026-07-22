"""
Module for finding the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(n):
    """Checks if a given number reads the same forwards and backwards."""
    return str(n) == str(n)[::-1]


def find_largest_palindrome():
    """
    Finds and returns the largest palindrome product of two 3-digit numbers,
    along with the two factors.
    """
    largest_palindrome = 0

    # Start from the largest 3-digit number and work downwards
    for i in range(999, 99, -1):

        # Start j at i to avoid redundant calculations (e.g., 900*999 vs 999*900)
        for j in range(i, 99, -1):
            product = i * j

            # If the product is smaller than our current best, stop checking this inner loop
            if product <= largest_palindrome:
                break

            if is_palindrome(product):
                largest_palindrome = product

    return largest_palindrome


if __name__ == "__main__":
    RESULT = find_largest_palindrome()
    print(RESULT)
