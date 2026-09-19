# Program to left rotate a list by one position

lst = []

n = int(input("Enter number of elements: "))

# Input the elements of the list
for i in range(n):
    x = int(input("Enter element: "))
    lst.append(x)

# Store the first element temporarily
temp = lst[0]

# Shift all elements one position to the left
for i in range(len(lst) - 1):
    lst[i] = lst[i + 1]

# Place the first element at the end
lst[-1] = temp

print("Left rotated list:", lst)