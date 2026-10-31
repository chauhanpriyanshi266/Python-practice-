# Program to find the first repeating element in a tuple

tup = tuple(map(int, input("Enter elements: ").split()))

# Find the first element that occurs more than once
for i in tup:
    if tup.count(i) > 1:
        print("First repeating element:", i)
        break
else:
    print("No repeating element found.")