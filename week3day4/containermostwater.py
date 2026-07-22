"""
max area of water a container can storeusing two-pointer approach
"""


def max_area(height: list[int]) -> int:
    """
    max-water=0
    for i in range(len(height)):
        for j in range(i+1,len(height)):
            current_area=min(height[i],height[j])*(j-i)
            max_water=max(max_water,current-area)

    return max-water
    """
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        current_water = min(height[left], height[right]) * (right - left)

        max_water = max(max_water, current_water)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water
