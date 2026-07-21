"""practicing binary search"""


def binary_search_iterative(nums: list[int], target: int) -> int:
    """binary search via iteration"""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def binary_search_recursive(
    nums: list[int], target: int, left: int = 0, right: int = None
) -> int:
    """binary search via recursion"""

    if right is None:
        right = len(nums) - 1

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if nums[mid] == target:
        return mid

    if nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)

    return binary_search_recursive(nums, target, left, mid - 1)
