def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_half = merge_sort(nums[:mid])
    right_half = merge_sort(nums[mid:])

    return merge(left_half, right_half)


def merge(left: list[int], right: list[int]) -> list[int]:
    sorted_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array
