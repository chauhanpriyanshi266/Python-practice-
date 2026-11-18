# Program to find missing numbers from a tuple of distinct integers
# within a known consecutive range

tup = tuple(map(int, input("Enter elements: ").split()))

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

result = []

# Check every number in the given range
for i in range(start, end + 1):

    if i not in tup:
        result.append(i)

# Display the missing numbers
print("Missing numbers:", result)