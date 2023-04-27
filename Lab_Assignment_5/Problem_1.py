def sortedSquares(A):
    n = len(A)
    res = [0] * n
    left, right = 0, n-1
    i = n-1
    while left <= right:
        if abs(A[left]) > abs(A[right]):
            res[i] = A[left] ** 2
            left += 1
        else:
            res[i] = A[right] ** 2
            right -= 1
        i -= 1
    return res[::-1]


# Test Case 1
A = [-6, -3, -1, 2, 4, 5]
print(sortedSquares(A))  # Output: [1, 4, 9, 16, 25, 36]

# Test Case 2
A = [-5, -4, -2, 0, 1]
print(sortedSquares(A))  # Output: [0, 1, 4, 16, 25]
