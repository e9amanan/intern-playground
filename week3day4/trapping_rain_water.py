def trap(height:list[int])-> int:
    """
    if not height:return 0
    water=0
    for i in range(len(height)):
        left_max=max(height[:i+1])
        right_max=max(height[i:])
        water+= min(left_max,right_max)-height[i]
    return water
"""

    if not height:
        return 0

    left=0
    right=len(height)-1

    left_max=height[left]
    right_max=height[right]

    total_water=0

    while left < right:

        if left_max < right_max:
            left+=1

            left_max=max(left_max,height[left])

            total_water+= left_max - height[left]

        else:
            right-=1

            right_max=max(right_max,height[right])

            total_water+= right_max - height[right]

    return total_water