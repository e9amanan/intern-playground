"""
Module for finding the second largest number in a list.
"""


def second_largest(nums):
    """Returns the second largest unique number from a list, or None if not possible."""
    unique_nums = list(set(nums))
    if len(unique_nums) < 2:
        return None

    unique_nums.sort()
    return unique_nums[-2]


if __name__ == "__main__":
    print(second_largest([10, 20, 4, 45, 99, 99, 45]))
