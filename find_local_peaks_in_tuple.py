# Program to find elements greater than both their immediate neighbours

tup = tuple(map(int, input("Enter elements: ").split()))

result = []

# Check elements that have neighbours on both sides
for i in range(1, len(tup) - 1):
    if tup[i] > tup[i - 1] and tup[i] > tup[i + 1]:
        result.append(tup[i])

# Display the local peaks as a tuple
print("Elements greater than both neighbours:", tuple(result))