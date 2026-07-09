import math


def compute_lcm(a, b):
    return (a * b) // math.gcd(a, b)


smallest_multiple = 1


for i in range(1, 21):

    smallest_multiple = compute_lcm(smallest_multiple, i)

print(f"{smallest_multiple}")
