"""
Module for finding the special Pythagorean triplet where a + b + c = 1000.
"""


def find_pythagorean_product(target_sum):
    """
    Finds the Pythagorean triplet (a, b, c) that sums to the target_sum,
    and returns a tuple containing the triplet and their product.
    """
    # 'a' must be strictly less than a third of the sum
    for a in range(1, (target_sum // 3) + 1):
        
        # 'b' must be greater than 'a', but less than half the sum
        for b in range(a + 1, target_sum // 2):
            
            c = target_sum - a - b

            if a**2 + b**2 == c**2:
                product = a * b * c
                return a, b, c, product

    return None


if __name__ == "__main__":
    TARGET = 1000
    RESULT = find_pythagorean_product(TARGET)
    
    if RESULT:
        triplet_a, triplet_b, triplet_c, abc_product = RESULT
        print(f"The triplet is: a={triplet_a}, b={triplet_b}, c={triplet_c}")
        print(f"The product abc is: {abc_product}")