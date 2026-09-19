# Program to remove consecutive duplicate elements from a list

lst = []
result = []

n = int(input("Enter number of elements: "))

# Input the elements of the list
for i in range(n):
    x = int(input("Enter element: "))
    lst.append(x)

# Remove consecutive duplicate elements
for i in lst:
    if len(result) == 0 or result[-1] != i:
        result.append(i)

print("List after removing consecutive duplicates:", result)