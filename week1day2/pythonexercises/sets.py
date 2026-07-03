def common_elements(list1: list, list2: list) -> set:
    return set(list1).intersection(set(list2))


def unique_chars(s: str) -> set[str]:
    return set(s)


def is_subset(set1: set, set2: set) -> bool:
    return set1.issubset(set2)