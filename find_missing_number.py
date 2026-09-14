# Program to find the missing number from a list

lst = []
n = int(input("Enter the number of elements: "))

# Input the elements of the list
for i in range(n):
    lst.append(int(input("Enter element: ")))

# Find the missing number from 1 to n + 1
for i in range(1, n + 2):
    if i not in lst:
        print("Missing number:", i)