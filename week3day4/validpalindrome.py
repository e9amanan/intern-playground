"""cleaned=s.replace(" ","").lower()
return cleaned == cleaned[::-1]"""


def is_palindrome(s: str) -> bool:
    """Return True if the string is a palindrome, ignoring
    non-alphanumeric characters and case."""
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
