# Program to rotate a matrix by 90 degrees clockwise

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

matrix = []

# Input the elements of the matrix
for i in range(n):
    row = []
    for j in range(m):
        x = int(input("Enter element: "))
        row.append(x)
    matrix.append(row)

rotated = []

# Transpose the matrix and reverse each row
for i in range(m):
    row = []
    for j in range(n):
        row.append(matrix[j][i])
    row.reverse()
    rotated.append(row)

print("Matrix after 90-degree clockwise rotation:", rotated)