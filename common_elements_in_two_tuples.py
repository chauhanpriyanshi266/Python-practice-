# Program to find common elements in two tuples

tup1 = tuple(input("Enter elements for tuple 1: ").split())
tup2 = tuple(input("Enter elements for tuple 2: ").split())

result = []

# Find common elements
for i in tup1:
    if i in tup2 and i not in result:
        result.append(i)

print("Common elements:", tuple(result))