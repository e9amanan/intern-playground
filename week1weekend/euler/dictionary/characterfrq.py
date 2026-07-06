from collections import Counter

def char_frequency(s):
    return dict(Counter(s))


print(char_frequency("hello")) 