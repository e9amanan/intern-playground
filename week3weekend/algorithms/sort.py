def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) / 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
        j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(nums: list[int], low: int = 0, high: int = None) -> None:
    if high is None:
        high = len(nums) - 1

    if low < high:
        partition_index = partition(nums, low, high)

        quick_sort(nums, low, partition_index - 1)
        quick_sort(nums, partition_index + 1, high)


def partition(nums: list[int], low: int, high: int) -> int:
    pivot = nums[high]

    i = low - 1

    for j in range(low, high):
        if nums[j] <= pivot:
            i = i + 1

            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[high] = nums[high], nums[i + 1]

    return i + 1
