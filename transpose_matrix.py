# Program to create the transpose of a matrix

matrix = []

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

# Create each row of the matrix
for i in range(rows):
    row = []

    # Add elements to the current row
    for j in range(columns):
        element = int(input("Enter element: "))
        row.append(element)

    # Add the completed row to the matrix
    matrix.append(row)

print("Original matrix:", matrix)

# Create the transpose of the matrix
transpose = []

for i in range(columns):
    row = []

    for j in range(rows):
        row.append(matrix[j][i])

    transpose.append(row)

print("Transpose of the matrix:", transpose)