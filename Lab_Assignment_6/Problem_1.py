def find_element(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    row = 0
    col = cols - 1
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            print(f"Element {target} is found at position ({row}, {col})")
            row += 1
            col -= 1
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1


matrix = [[-4, -3, -1, 3, 5],
          [-3, -2, 2, 4, 6],
          [-1, 1, 3, 5, 8],
          [3, 4, 7, 8, 9]]

find_element(matrix, 3)

# Element 3 is found at position (0, 3)
# Element 3 is found at position (2, 2)
# Element 3 is found at position (3, 0)
