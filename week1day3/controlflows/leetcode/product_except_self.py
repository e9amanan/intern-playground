"""contains a solution for the LeetCode 'Product of Array Except Self' problem."""


def product_except_self(nums: list[int]) -> list[int]:
    """Calculates the product of all elements in the array except the one at the current index"""
    length = len(nums)
    answer = [1] * length

    curr_product = 1
    for i in range(length):
        answer[i] = curr_product
        curr_product *= nums[i]

    curr_product = 1
    for i in range(length - 1, -1, -1):
        answer[i] *= curr_product
        curr_product *= nums[i]

    return answer
