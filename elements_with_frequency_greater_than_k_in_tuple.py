# Program to find elements whose frequency is greater than k in a tuple

tup = tuple(map(int, input("Enter elements: ").split()))
k = int(input("Enter k: "))

result = []

# Find elements whose frequency is greater than k
for i in tup:
    frequency = tup.count(i)

    if frequency > k and i not in result:
        result.append(i)

# Display the result as a tuple
print("Elements with frequency greater than k:", tuple(result))