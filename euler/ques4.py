def is_palindrome(n):
    return str(n) == str(n)[::-1]


largest_palindrome = 0
factor_1 = 0
factor_2 = 0


for i in range(999, 99, -1):

    for j in range(i, 99, -1):
        product = i * j

        if product <= largest_palindrome:
            break

        if is_palindrome(product):
            largest_palindrome = product
            factor_1 = i
            factor_2 = j

print(f"{largest_palindrome}")
