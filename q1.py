def first_stable_character(s):
    """
    Find the first stable character in the string.

    A character is stable if:
    1. It appears at least twice
    2. All occurrences are in one continuous group

    Args:
        s (str): Input string

    Returns:
        str or None: First stable character, or None if no stable character exists

    Examples:
        >>> first_stable_character("abccba")
        'c'
        >>> first_stable_character("abc")
        None
        >>> first_stable_character("a")
        None
    """
    if len(s) == 0:
        return None
    i = 0
    while i < len(s):
        char = s[i]
        count = 1
        j = i + 1
        while j < len(s) and s[j] == char:
            count = count + 1
            j = j + 1
        appears_later = False
        for k in range(j, len(s)):
            if s[k] == char:
                appears_later = True
                break
        if count >= 2 and not appears_later:
            return char
        i = i + 1
    return None
if __name__ == "__main__":
    # Test your solution here
    print(first_stable_character("abccba"))      # Should print: c
    print(first_stable_character("abc"))         # Should print: None
    print(first_stable_character("a"))           # Should print: None
    print(first_stable_character("aaabccddde"))  # Should print: a
    print(first_stable_character("aabbcc"))      # Should print: a
