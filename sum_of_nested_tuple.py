# Program to find the total sum of elements in a nested tuple

n = int(input("Enter number of inner tuples: "))

nested = []

# Create the nested tuple
for i in range(n):
    a = int(input("Enter first element: "))
    b = int(input("Enter second element: "))
    nested.append((a, b))
tup = tuple(nested)

total = 0

# Calculate the sum of all elements
for i in range(len(tup)):
    for j in range(len(tup[i])):
        total = total + tup[i][j]

print("Total sum:", total)