# Program to extract all prime numbers from a tuple

tup = tuple(map(int, input("Enter elements: ").split()))

result = []

# Check each element for primality
for i in tup:
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result.append(i)

# Convert the result list into a tuple
print("Prime numbers:", tuple(result))