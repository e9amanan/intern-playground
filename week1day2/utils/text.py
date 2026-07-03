def clean_text(s: str) ->str:
    words_list=s.strip().lower().split()
    return " ".join(words_list)

def tokenizer(s:str,delimiter:str=" ") -> list[str]:
    return s.split(delimiter)

def count_chars(s: str)-> dict[str,int]:
    char_map: dict[str,int] = {}

    for char in s:
        char_map[char] = char_map.get(char,0)+1

    return char_map




