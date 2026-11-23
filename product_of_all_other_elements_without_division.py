# Program to find the product of all other elements without division

tup = tuple(map(int, input("Enter elements: ").split()))
result = []

# Calculate the product excluding each element
for i in range(len(tup)):
    el = 1

    for j in range(len(tup)):
        if i == j:
            continue
        else:
            el *= tup[j]

    result.append(el)

# Display the result
print("Product of all other elements:", tuple(result))