def invert_dict(d: dict[str,str]) -> dict[str,str]:
    inverted={}
    for k,v in d.items():
        inverted[v] = k
    return inverted


def merge_dicts(*dicts:dict) -> dict:
    merged={}
    for d in dicts:
        merged.update(d)
    return merged


