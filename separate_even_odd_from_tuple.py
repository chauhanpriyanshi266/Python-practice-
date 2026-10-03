# Program to separate even and odd elements from a tuple

tup = tuple(map(int, input("Enter elements: ").split()))

even = []
odd = []

# Separate even and odd elements
for i in tup:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even:", tuple(even))
print("Odd:", tuple(odd))