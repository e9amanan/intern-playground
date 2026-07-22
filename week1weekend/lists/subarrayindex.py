"""
Module for finding a contiguous subarray that sums to a specific target.
"""


def subarray_sum(arr, target):
    """
    Finds a continuous sub-array that adds up to a given target.
    Returns the 1-based starting and ending indices, or [-1] if not found.
    """
    current_sum = 0
    start = 0

    for end in range(len(arr)):
        current_sum += arr[end]

        while current_sum > target and start <= end:
            current_sum -= arr[start]
            start += 1

        if current_sum == target:
            return [start + 1, end + 1]

    return [-1]


if __name__ == "__main__":
    print(subarray_sum([1, 2, 3, 7, 5], 12))
