# Program to merge two sorted tuples without using sort() or sorted()

tup1 = tuple(map(int, input("Enter elements for tup1: ").split()))
tup2 = tuple(map(int, input("Enter elements for tup2: ").split()))

result = []

i = 0
j = 0

# Compare elements from both tuples
while i < len(tup1) and j < len(tup2):

    if tup1[i] <= tup2[j]:
        result.append(tup1[i])
        i += 1

    else:
        result.append(tup2[j])
        j += 1

# Add remaining elements from the first tuple
while i < len(tup1):
    result.append(tup1[i])
    i += 1

# Add remaining elements from the second tuple
while j < len(tup2):
    result.append(tup2[j])
    j += 1

# Display the merged tuple
print("Merged tuple:", tuple(result))