"""
Module for calculating the sum of even Fibonacci numbers using an optimized recurrence relation.
"""


def even_fibo_optimized(limit):
    """
    Calculates the sum of even Fibonacci numbers up to the limit by 
    directly generating only the even terms.
    """
    a, b = 2, 8
    total_sum = 0
    
    while a <= limit:
        total_sum += a
        # Generate the next even Fibonacci number directly
        a, b = b, 4 * b + a
        
    return total_sum


if __name__ == "__main__":
    LIMIT_VALUE = 4000000
    RESULT = even_fibo_optimized(LIMIT_VALUE)
    print(RESULT)