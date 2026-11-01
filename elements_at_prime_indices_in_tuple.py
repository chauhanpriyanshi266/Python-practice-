# Program to find elements at prime-numbered indices in a tuple

tup = tuple(map(int, input("Enter elements: ").split()))

result = []

# Check each index to determine whether it is prime
for i in range(2, len(tup)):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        # Add the element if its index is prime
        result.append(tup[i])

# Display the result as a tuple
print("Elements at prime indices:", tuple(result))