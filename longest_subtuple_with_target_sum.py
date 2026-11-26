# Program to find the longest contiguous subtuple with a given target sum

tup = tuple(map(int, input("Enter elements: ").split()))
target = int(input("Enter target sum: "))

longest = ()

# Generate all possible contiguous subtuples
for i in range(len(tup)):
    for j in range(i, len(tup)):
        total = 0

        # Calculate the sum of the current subtuple
        for k in range(i, j + 1):
            total += tup[k]

        # Check whether the sum equals the target
        if total == target:

            # Update if a longer subtuple is found
            if j - i + 1 > len(longest):
                longest = tup[i:j+1]

# Display the result
if longest:
    print("Longest subtuple:", longest)
    print("Length:", len(longest))
else:
    print("No subtuple found with the given target sum.")