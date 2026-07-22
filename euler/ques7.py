"""
Module for calculating and finding the Nth prime number.
"""


def is_prime(num):
    """
    Checks if a number is prime by testing factors up to its square root.
    """
    if num < 2:
        return False

    # Check every number from 2 up to the square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Found a factor, so it is not prime

    return True  # No factors found, it is prime


def find_nth_prime(n):
    """
    Iterates through integers to find and return the Nth prime number.
    """
    prime_count = 0
    current_number = 1

    # Keep going until we have found the Nth prime
    while prime_count < n:
        current_number += 1
        if is_prime(current_number):
            prime_count += 1

    return current_number


if __name__ == "__main__":
    TARGET_PRIME = 10001
    RESULT = find_nth_prime(TARGET_PRIME)
    print(f"The {TARGET_PRIME}st prime number is: {RESULT}")
