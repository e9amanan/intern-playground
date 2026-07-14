"""
n = 100

sum_of_squares = sum(i**2 for i in range(1, n + 1))

square_of_sum = sum(range(1, n + 1)) ** 2

difference = square_of_sum - sum_of_squares

print(f"{difference}")
"""

def sum_square_difference_optimized(n):
    
    sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6
    square_of_sum = ((n * (n + 1)) // 2) ** 2
    
    return square_of_sum - sum_of_squares

print(sum_square_difference_optimized(100))