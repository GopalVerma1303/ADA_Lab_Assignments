def isMatch(text, pattern):
    # Create a 2D array to store the results of matching the pattern to the text
    dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

    # Base case: an empty pattern matches an empty text
    dp[0][0] = True

    # Deal with patterns that start with '*'
    for j in range(1, len(pattern) + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Fill in the rest of the table
    for i in range(1, len(text) + 1):
        for j in range(1, len(pattern) + 1):
            if pattern[j - 1] in {text[i - 1], '.'}:
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                dp[i][j] = dp[i][j -
                                 2] or (dp[i - 1][j] and pattern[j - 2] in {text[i - 1], '.'})

    # Return the final result
    return dp[-1][-1]
