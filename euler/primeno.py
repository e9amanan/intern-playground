def is_prime(num):
    """
    Checks if a number is prime.
    We only need to test factors up to the square root of the number.
    """
    if num < 2:
        return False
    
    # Check every number from 2 up to the square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Found a factor, so it's not prime
            
    return True  # No factors found, it is prime

# Set up our counters
prime_count = 0
current_number = 1

# Keep going until we have found 10,001 primes
while prime_count < 10001:
    current_number += 1
    if is_prime(current_number):
        prime_count += 1

print(f"The 10,001st prime number is: {current_number}")