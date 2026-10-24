# Program to find the cumulative sum of elements in a tuple

tup = tuple(map(int, input("Enter elements: ").split()))

total = 0
result = []

# Calculate the cumulative sum
for i in tup:
    total += i
    result.append(total)

# Convert the result list into a tuple
print("Cumulative sum tuple:", tuple(result))