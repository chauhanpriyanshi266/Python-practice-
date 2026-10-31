# Program to find all non-repeating elements in a tuple

tup = tuple(map(int, input("Enter elements: ").split()))

result = []

# Find elements that occur only once
for i in tup:
    if tup.count(i) == 1:
        result.append(i)

# Display all non-repeating elements
print("All non-repeating elements:", tuple(result))