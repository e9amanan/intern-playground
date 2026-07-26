"""find the contiguous subarray with the largest sum"""


def max_subarray(nums: list[int]) -> int:
    """
    max_sum=0
    for i in range(len(nums)):
        current_sum=0
        for j in range(i,len(nums)):
            current_sum += nums[j]
            max_sum=max(max_sum,current_sum)
    return max_sum
    """
    max_sum = 0
    current_sum = 0

    for num in nums:
        current_sum = max(current_sum, 0)
        currentsum += num

        max_sum = max(max_sum, current_sum)

    return max_sum
