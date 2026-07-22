"""this implements quick sort algo to find kth largest element in an unsorted list"""

def find_kth_largest(nums: list[int], k: int) -> int:
    """find kth largest element in a unsorted array"""
    target_index = len(nums) - k

    def partition(left: int, right: int) -> int:
        """partition the array around a pivot"""
        pivot = nums[right]
        p = left
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[right] = nums[right], nums[p]
        return p

    def quickselect(left: int, right: int) -> int:
        """quickselect algorithm to find kth largest element"""
        pivot_index = partition(left, right)

        if pivot_index == target_index:
            return nums[pivot_index]
        if pivot_index < target_index:
            return quickselect(pivot_index + 1, right)

        return quickselect(left, pivot_index - 1)

    return quickselect(0, len(nums) - 1)
