""" def even_fibo(limit):
    a, b = 1, 2
    total_sum = 0

    while a <= limit:
        if a % 2 == 0:
            total_sum += a
        a, b = b, a + b

    return total_sum


limit_value = 4000000

result = even_fibo(limit_value)

print(result)"""

def even_fibo_optimized(limit):
    a, b = 2, 8
    total_sum = 0
    
    while a <= limit:
        total_sum += a
        a, b = b, 4 * b + a
        
    return total_sum