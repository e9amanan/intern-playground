"""to find first occurence via binary search"""


def find_first_occurence(nums: list[int], target: int) -> int:
    """to find first occurence via binary search"""
    left, right = 0, len(nums) - 1

    first_pos = -1
    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            first_pos = mid
            right = mid - 1

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return first_pos
