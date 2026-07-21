def quick_sort(nums:list[int],low:int=0,high: int =None)-> None:
    if high is None:
        high=len(nums)-1

    if low<high:
        partition_index=partition(nums,low,high)

        quick_sort(nums,low,partition_index - 1)
        quick_sort(nums,partition_index+1,high)

def partition(nums:list[int],low:int,high:int)->int:
    pivot =nums[high]

    i=low-1

    for j in range(low,high):
        if nums[j] <= pivot:
            i=i+1

            nums[i],nums[j] = nums[j],nums[i]

    nums[i+1],nums[high] = nums[high],nums[i+1]

    return i+1