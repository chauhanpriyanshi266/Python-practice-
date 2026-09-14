# Program to reverse a list without using reverse()

lst = []
rev = []

n = int(input("Enter number of elements for the list: "))

# The loop runs n times for the list
for i in range(n):
    lst.append(int(input("Enter element: ")))

# Traverse the list from the last index to the first
for i in range(len(lst) - 1, -1, -1):
    rev.append(lst[i])

print("Reversed list:", rev)