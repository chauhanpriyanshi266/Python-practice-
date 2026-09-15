# Program to create and print a 2D list

matrix = []

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

# Create each row
for i in range(n):
    row = []

    # Add elements to the current row
    for j in range(m):
        x = int(input("Enter element: "))
        row.append(x)

    # Add the completed row to the matrix
    matrix.append(row)

print("2D list is:", matrix)