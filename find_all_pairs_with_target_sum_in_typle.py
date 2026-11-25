# Program to find all pairs in a tuple with a given target sum

tup = tuple(map(int, input("Enter elements: ").split()))
target = int(input("Enter target sum: "))

result = []

# Find all pairs whose sum equals the target
for i in range(len(tup)):
    for j in range(i + 1, len(tup)):

        if tup[i] + tup[j] == target:
            result.append((tup[i], tup[j]))

# Display the matching pairs
print("Pairs with target sum:", tuple(result))