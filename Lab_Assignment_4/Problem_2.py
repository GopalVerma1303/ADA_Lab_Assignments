def is_match(text, pattern):
    # Base case: if both text and pattern are empty, then it's a match
    if not text and not pattern:
        return True

    # Recursive cases
    if pattern and pattern[0] == '*':
        # Case 1: matching zero preceding character of '*'
        if is_match(text, pattern[1:]):
            return True
        # Case 2: matching one or more preceding character of '*'
        i = 0
        while i < len(text) and (pattern[1] == '.' or text[i] == pattern[1]):
            if is_match(text[i+1:], pattern[2:]):
                return True
            i += 1
    elif text and pattern and (pattern[0] == '.' or text[0] == pattern[0]):
        # Case 3: matching a single character from lowercase alphabetic characters
        if is_match(text[1:], pattern[1:]):
            return True

    # All recursive cases failed, so it's not a match
    return False
