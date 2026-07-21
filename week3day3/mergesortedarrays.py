"""merge 2 sorted arrays"""


def merge(arr1: list[int], m: int, arr2: list[int]) -> list[int]:
    """using list slicing"""
    arr1[m:] = arr2
    return arr1.sort()
