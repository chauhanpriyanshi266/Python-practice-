# Program to find the sum of all elements in a 2D list

matrix = []

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

# Create the 2D list row by row
for i in range(n):
    row = []

    # Add elements to the current row
    for j in range(m):
        x = int(input("Enter element: "))
        row.append(x)

    # Add the completed row to the matrix
    matrix.append(row)

total = 0

# Calculate the sum of all elements
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        total += matrix[i][j]

print("2D list is:", matrix)
print("Sum of all elements:", total)