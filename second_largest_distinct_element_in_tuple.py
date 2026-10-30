# Program to find the second-largest distinct element in a tuple

tup = tuple(map(int, input("Enter elements: ").split()))

# Remove duplicate elements
unique_elements = set(tup)

# Sort the unique elements
sorted_elements = sorted(unique_elements)

# Find the second-largest element
if len(sorted_elements) >= 2:
    print("Second-largest element:", sorted_elements[-2])
else:
    print("Second-largest element does not exist.")