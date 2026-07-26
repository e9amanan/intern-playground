def three_sum(nums: list[int]) -> list[list[int]]:
    result = []
    nums.sort()

    for i, num in enumerate(nums):
        if num > 0:
            break

        if i > 0 and num == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            three_sum_val = num + nums[left] + nums[right]

            if three_sum_val < 0:
                left += 1
            elif three_sum_val > 0:
                right -= 1
            else:
                result.append([num, nums[left], nums[right]])

                left += 1
                right -= 1

                # Skip duplicate values for the left pointer
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Skip duplicate values for the right pointer
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return result
