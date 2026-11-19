# Program to find the longest string(s) in a tuple

tup = tuple(input("Enter elements: ").split())

maximum_length = 0
result = []

# Find the maximum length
for i in tup:
    if len(i) > maximum_length:
        maximum_length = len(i)

# Find all strings having the maximum length
for i in tup:
    if len(i) == maximum_length:
        result.append(i)

# Display the result
print("Longest string(s):", tuple(result))