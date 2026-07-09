"""Write utils/collections.py with functions

Function specs
    frequencies(items: list[str]) -> dict[str, int]
        Input: list of strings
        Output: dict mapping item -> count
        Example: ["a","b","a"] -> {"a": 2, "b": 1}
    dedupe(items: list[str]) -> list[str]
        Input: list with duplicates
        Output: list preserving first occurrence order
        Example: ["a","b","a"] -> ["a","b"]
    group_by(items: list[dict], key: str) -> dict[str, list[dict]]
        Input: list of dicts, key to group by
        Output: dict mapping key values to lists of items
        Example: [{"status":"todo","id":1}, {"status":"done","id":2}] grouped by "status"

"""


def frequencies(items: list[str]) -> dict[str, int]:
    freq_map: dict[str, int] = {}

    for c in items:
        freq_map[c] = freq_map.get(c, 0) + 1

    return freq_map


def deduce(items: list[str]) -> list[str]:
    return list(dict.fromkeys(items))


def group_by(items: list[dict], key: str) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {}

    for item in items:
        group_key = item.get(key)

        if group_key not in grouped:
            grouped[group_key] = []

        grouped[group_key].append(item)

    return grouped
