# Program to sort the elements of a tuple in ascending order and create a new tuple

tup = tuple(map(int, input("Enter elements: ").split()))

l = list(tup)
l.sort()

result = tuple(l)

print("Sorted tuple:", result)