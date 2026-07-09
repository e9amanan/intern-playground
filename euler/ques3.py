def prime_factor(n):
    factor = 2

    while factor * factor <= n:
        if n % factor == 0:
            n = n / factor
        else:
            factor += 1

    return n


target_number = 600851475143


result = prime_factor(target_number)
print(result)
