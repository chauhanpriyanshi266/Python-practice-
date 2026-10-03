# Program to remove duplicate elements from a tuple

tup = tuple(input("Enter elements: "))

result = []

# Add only unique elements to the result
for i in range(len(tup)):
    if tup[i] not in result:
        result.append(tup[i])

print("Tuple after removing duplicates:", tuple(result))