"""to find first occurence via binary search"""


def find_last_occurence(nums: list[int], target: int) -> int:
    """to find last occurence via binary search"""
    left, right = 0, len(nums) - 1

    last_pos = -1
    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            last_pos = mid
            left = mid + 1

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return last_pos
