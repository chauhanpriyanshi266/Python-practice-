# Program to check whether one list is a subset of another list

lst1 = []
lst2 = []

n = int(input("Enter number of elements for the first list: "))

# The loop runs n times for the first list
for i in range(n):
    x = int(input("Enter element: "))
    lst1.append(x)

m = int(input("Enter number of elements for the second list: "))

# The loop runs m times for the second list
for i in range(m):
    y = int(input("Enter element: "))
    lst2.append(y)

# Check whether every element of lst1 is present in lst2
for i in lst1:
    if i not in lst2:
        print("The first list is not a subset of the second list.")
        break
else:
    print("The first list is a subset of the second list.")