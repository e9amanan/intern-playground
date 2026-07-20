"""
Module for calculating the difference between the sum of the squares 
and the square of the sum of the first N natural numbers.
"""


def sum_square_difference_optimized(n):
    """
    Calculates the sum square difference in O(1) time complexity 
    using mathematical progression formulas.
    """
    sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6
    square_of_sum = ((n * (n + 1)) // 2) ** 2
    
    return square_of_sum - sum_of_squares


if __name__ == "__main__":
    LIMIT = 100
    RESULT = sum_square_difference_optimized(LIMIT)
    print(RESULT)