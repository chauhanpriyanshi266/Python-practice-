# Program to find the second largest and second smallest elements from a tuple

tup = tuple(map(int, input("Enter elements: ").split()))

l = list(tup)
l.sort()

print("Second largest:", l[-2])
print("Second smallest:", l[1])