# Program to print a matrix in spiral order

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

matrix = []

# Input the matrix
for i in range(n):
    row = []

    for j in range(m):
        x = int(input("Enter element: "))
        row.append(x)

    matrix.append(row)

top = 0
bottom = n - 1
left = 0
right = m - 1

# Traverse the matrix in spiral order
while top <= bottom and left <= right:

    # Traverse the top row
    for j in range(left, right + 1):
        print(matrix[top][j])

    top += 1

    # Traverse the right column
    for k in range(top, bottom + 1):
        print(matrix[k][right])

    right -= 1

    # Traverse the bottom row
    for l in range(right, left - 1, -1):
        print(matrix[bottom][l])

    bottom -= 1

    # Traverse the left column
    for p in range(bottom, top - 1, -1):
        print(matrix[p][left])

    left += 1