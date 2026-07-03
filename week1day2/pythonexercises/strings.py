def is_palindrome(s: str)-> bool:
    cleaned=s.replace(" ","").lower()
    return cleaned==cleaned[::-1]

def reverse_words(s:str)->str:
    words=s.split()
    reversed=words[::-1]
    return " ".join(reversed)


def title_case(s:str )-> str:
    words=s.split()
    new_words=[]

    for word in words:
        new_word=word[0].upper()+word[1:]
        new_words.append(new_word)

    return " ".join(new_words)

