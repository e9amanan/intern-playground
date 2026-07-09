"""Function specs

clean_text(s: str) -> str
    Input: raw string with extra spaces, mixed case, punctuation
    Output: normalized lowercase string with single spaces and trimmed ends
    Example: " Hello, WORLD! " -> "hello, world!"
tokenize(s: str, delimiter: str = " ") -> list[str]
    Input: text string, optional delimiter (default space)
    Output: list of word tokens split on delimiter
    Example: "hello, world!" -> ["hello,", "world!"]
count_chars(s: str) -> dict[str, int]
    Input: string
    Output: character frequency map
    Example: "hello" -> {"h": 1, "e": 1, "l": 2, "o": 1}
"""


def clean_text(s: str) -> str:
    words_list = s.strip().lower().split()
    return " ".join(words_list)


def tokenize(s: str, delimiter: str = " ") -> list[str]:
    return s.split(delimiter)


def count_chars(s: str) -> dict[str, int]:
    char_map: dict[str, int] = {}

    for char in s:
        char_map[char] = char_map.get(char, 0) + 1

    return char_map
