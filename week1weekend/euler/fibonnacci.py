"""
Module for calculating the sum of even Fibonacci numbers up to a specified limit.
"""


def even_fibo(limit):
    """
    Generates Fibonacci numbers up to the limit and returns the sum
    of only the even-valued terms.
    """
    a, b = 1, 2
    total_sum = 0

    while a <= limit:
        if a % 2 == 0:
            total_sum += a

        # Tuple unpacking allows simultaneous assignment without a temporary variable
        a, b = b, a + b

    return total_sum


if __name__ == "__main__":
    LIMIT_VALUE = 4000000
    RESULT = even_fibo(LIMIT_VALUE)
    print(RESULT)
