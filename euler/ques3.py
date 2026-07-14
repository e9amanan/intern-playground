"""def prime_factor(n):
    factor = 2

    while factor * factor <= n:
        if n % factor == 0:
            n = n / factor
        else:
            factor += 1

    return n


target_number = 600851475143


result = prime_factor(target_number)
print(result)"""

def prime_factor_optimized(n):
    
    while n % 2 == 0:
        n = n // 2
        
    if n == 1:
        return 2
        
    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            n = n // factor
        else:
            factor += 2 
    return int(n)