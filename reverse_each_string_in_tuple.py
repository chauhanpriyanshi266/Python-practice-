# Program to reverse every string inside a tuple

tup = tuple(input("Enter elements: ").split())

result = []

# Reverse each string
for i in tup:
    reverse = i[::-1]
    result.append(reverse)

# Display the reversed strings as a tuple
print("Reversed strings:", tuple(result))