"""to find the longest subarray with distinct characters"""


def length_of_longest_substring(s: str) -> int:
    """
    max_len=0
    for i in range(len(s)):
        for j in range(i,len(s)):
        substring=s[i:j+1]
        if len(set(substring))==len(substring):
        max_len=max(max_len,len(substring))
    return max_len
    """

    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        current_window_size = right - left + 1
        max_length = max(max_length, current_window_size)

    return max_length
