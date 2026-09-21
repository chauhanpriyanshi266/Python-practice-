# Program to find the intersection of two lists with duplicates

lst1 = []
lst2 = []

n = int(input("Enter number of elements for the first list: "))

# Input the elements of the first list
for i in range(n):
    x = int(input("Enter element: "))
    lst1.append(x)

m = int(input("Enter number of elements for the second list: "))

# Input the elements of the second list
for i in range(m):
    y = int(input("Enter element: "))
    lst2.append(y)

freq = {}
result = []

# Count the frequency of each element in the first list
for i in lst1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

# Find common elements while considering their frequency
for element in lst2:
    if element in freq and freq[element] > 0:
        result.append(element)
        freq[element] -= 1

print("Intersection with duplicates:", result)