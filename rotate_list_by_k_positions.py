# Program to right rotate a list by k positions

lst = []

n = int(input("Enter number of elements: "))

# Input the elements of the list
for i in range(n):
    x = int(input("Enter element: "))
    lst.append(x)

k = int(input("Enter k: "))

first = lst[0:-k]
last = lst[-k:]

print("Rotated list:", last + first)