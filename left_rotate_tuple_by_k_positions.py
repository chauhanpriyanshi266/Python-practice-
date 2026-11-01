# Program to rotate a tuple k positions to the left

tup = tuple(map(int, input("Enter elements: ").split()))
k = int(input("Enter k: "))

# Handle k values greater than the tuple length
k = k % len(tup)

# Rotate the tuple to the left
result = tup[k:] + tup[:k]

print("Tuple after left rotation:", result)