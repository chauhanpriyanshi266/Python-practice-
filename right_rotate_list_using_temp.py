# Program to right rotate a list by one position

lst = []

n = int(input("Enter number of elements: "))

# Input the elements of the list
for i in range(n):
    x = int(input("Enter element: "))
    lst.append(x)

# Store the last element temporarily
temp = lst[-1]

# Shift all elements one position to the right
for i in range(len(lst) - 1, 0, -1):
    lst[i] = lst[i - 1]

# Place the last element at the first position
lst[0] = temp

print("Right rotated list:", lst)