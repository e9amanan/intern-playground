"""
Module for calculating the sum of multiples of 3 or 5 below 1000.
"""


def calculate_multiples_sum():
    """
    Calculates the sum of all multiples of 3 or 5 below 1000 using 
    arithmetic progression, returning the exact integer result.
    """
    # Using integer division (//) to avoid float conversion
    s_3 = 333 // 2 * (6 + (333 - 1) * 3)
    s_5 = 199 // 2 * (10 + (199 - 1) * 5)
    s_15 = 66 // 2 * (30 + (66 - 1) * 15)
    
    return s_5 + s_3 - s_15


if __name__ == "__main__":
    ANS = calculate_multiples_sum()
    print(ANS)