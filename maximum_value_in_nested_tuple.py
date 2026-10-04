# Program to find the maximum value in a nested tuple

n = int(input("Enter number of inner tuples: "))

nested = []

# Create the nested tuple
for i in range(n):
    a = int(input("Enter first element: "))
    b = int(input("Enter second element: "))
    c = int(input("Enter third element: "))
    nested.append((a, b, c))

tup = tuple(nested)

maximum = tup[0][0]

# Find the maximum value
for i in range(len(tup)):
    for j in range(len(tup[i])):
        if tup[i][j] > maximum:
            maximum = tup[i][j]

print("Maximum:", maximum)