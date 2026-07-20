"""
Module for calculating the largest prime factor of a given number.
"""


def prime_factor_optimized(n):
    """
    Finds the largest prime factor of a given integer by stripping 
    factors of 2 first, then checking only odd factors.
    """
    # 1. Strip out all factors of 2 immediately
    while n % 2 == 0:
        n = n // 2
        
    # If the number was a pure power of 2, the largest prime factor is 2
    if n == 1:
        return 2
        
    # 2. Check only odd factors, starting at 3
    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            n = n // factor
        else:
            # Skip all even numbers
            factor += 2 
            
    return int(n)


if __name__ == "__main__":
    TARGET_NUMBER = 600851475143
    RESULT = prime_factor_optimized(TARGET_NUMBER)
    print(RESULT)