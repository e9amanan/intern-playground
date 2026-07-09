def even_fibo(limit):
    a, b = 1, 2
    total_sum = 0

    while a <= limit:
        if a % 2 == 0:
            total_sum += a
        a, b = b, a + b

    return total_sum


limit_value = 4000000

result = even_fibo(limit_value)

print(result)
