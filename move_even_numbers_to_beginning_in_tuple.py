# Program to move all even numbers to the beginning of a tuple

tup = tuple(map(int, input("Enter elements: ").split()))

even = []
odd = []

# Separate even and odd numbers
for i in tup:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

# Combine even and odd numbers and convert the result into a tuple
result = tuple(even + odd)

print("Tuple after moving even numbers to the beginning:", result)