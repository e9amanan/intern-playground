def frequencies(items: list[str])-> dict[str, int]:
    freq_map:dict[str,int]={}

    for c in items:
        freq_map[c]=freq_map.get(c,0)+1

    return freq_map


def deduce(items:list[str])->list[str]:
    return list(dict.fromkeys(items))

def group_by(items:list[dict],key:str)-> dict[str,list[dict]]:
    grouped: dict[str,list[dict]]={}

    for item in items:
        group_key=item.get(key)

        if group_key not in grouped:
            grouped[group_key]=[]

        grouped[group_key].append(item)

    return grouped





