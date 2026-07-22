"""practice of lists"""

"""def merge_sorted(list1: list[int], list2: list[int]) -> list[int]:
    i, j = 0, 0
    merged = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list[2])
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged"""


def merge_sorted_simple(list1: list[int], list2: list[int]) -> list[int]:
    return sorted(list1 + list2)


def chunk_list(items: list, size: int) -> list[list]:
    chunked = []
    for i in range(0, len(items), size):
        chunk = items[i : i + size]
        chunked.append(chunk)
    return chunked


"""def flatten(nested: list[list]) -> list:
    flat_list = []
    for sub_list in nested:
        for i in sub_list:
            flat_list.append(i)
    return flat_list"""


def flatten_simple(nested: list[list]) -> list:
    return [item for sublist in nested for item in sublist]
