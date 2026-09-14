# Program to find common elements between two lists

l1 = []
l2 = []

n = int(input("Enter number of elements for the first list: "))
m = int(input("Enter number of elements for the second list: "))

# The loop runs n times for the first list
for i in range(n):
    l1.append(int(input("Enter element: ")))

# The loop runs m times for the second list
for i in range(m):
    l2.append(int(input("Enter element: ")))

common = []

# Check each element of the first list in the second list
for i in l1:
    if i in l2 and i not in common:
        common.append(i)

print("Common elements:", common)