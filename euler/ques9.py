for a in range(1, 334):

    for b in range(a + 1, 500):

        c = 1000 - a - b

        if a**2 + b**2 == c**2:
            product = a * b * c
            print(f"The triplet is: a={a}, b={b}, c={c}")
            print(f"The product abc is: {product}")

            break
