# Program to create a frequency dictionary from a tuple

tup = tuple(input("Enter elements: ").split())

d = {}

# Count the frequency of each element
for i in tup:
    d[i] = tup.count(i)

print("Frequency dictionary:", d)