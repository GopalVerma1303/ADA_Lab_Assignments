def birthday_bombs(A, B):
    # calculate dp using dynamic programming
    dp = [0] + [-1] * A
    last_friend = [-1] * (A+1)
    for i in range(1, A+1):
        for j in range(len(B)):
            if B[j] <= i and dp[i-B[j]] != -1:
                if dp[i] < dp[i-B[j]] + 1:
                    dp[i] = dp[i-B[j]] + 1
                    last_friend[i] = j
                elif dp[i] == dp[i-B[j]] + 1:
                    # choose lexicographically smallest friend
                    if last_friend[i] == -1 or B[j] < B[last_friend[i]]:
                        last_friend[i] = j

    # construct the lexicographically smallest array
    result = []
    i = A
    while i > 0:
        j = last_friend[i]
        result.extend([j] * dp[i])
        i -= B[j] * dp[i]

    return result[::-1]


# example cases
print(birthday_bombs(12, [3, 4]))  # should print [0, 0, 0, 0]
print(birthday_bombs(11, [6, 8, 5, 4, 7]))  # should print [0, 2]
