# Program to find all duplicate elements in a tuple without repeating them

tup = tuple(map(int, input("Enter elements: ").split()))

result = []

# Find duplicate elements
for i in tup:
    frequency = tup.count(i)

    if frequency > 1 and i not in result:
        result.append(i)

# Display the duplicate elements
print("Duplicate elements:", tuple(result))