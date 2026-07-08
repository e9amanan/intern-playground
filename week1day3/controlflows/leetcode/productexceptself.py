def productExceptSelf(nums: list[int]) -> list[int]:
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