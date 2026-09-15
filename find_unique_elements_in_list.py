# Program to find unique elements in a list

lst = []
n = int(input("Enter the number of elements: "))

# Input the elements of the list
for i in range(n):
    lst.append(int(input("Enter element: ")))

print("Unique elements:")

# Find elements that occur only once
for i in lst:
    if lst.count(i) == 1:
        print(i)