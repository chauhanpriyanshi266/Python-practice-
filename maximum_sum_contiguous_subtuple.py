# Program to find the maximum sum and its contiguous subtuple

tup = tuple(map(int, input("Enter elements: ").split()))

maximum = float('-inf')
result = ()

# Generate all possible contiguous subtuples
for i in range(len(tup)):
    for j in range(i, len(tup)):
        total = 0

        # Calculate the sum of the current subtuple
        for k in range(i, j + 1):
            total += tup[k]

        # Update the maximum sum and subtuple
        if total > maximum:
            maximum = total
            result = tup[i:j+1]

# Display the result
print("Maximum sum:", maximum)
print("Subtuple:", result)