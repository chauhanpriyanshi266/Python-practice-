# Program to find the first non-repeating element in a tuple

tup = tuple(map(int, input("Enter elements: ").split()))

# Find the first element that occurs only once
for i in tup:
    if tup.count(i) == 1:
        print("First non-repeating element:", i)
        break
else:
    print("No non-repeating element found.")