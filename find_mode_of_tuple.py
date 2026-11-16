# Program to find the mode(s) of a tuple
# Return all modes if there is a tie

tup = tuple(map(int, input("Enter elements: ").split()))

result = []
maximum_frequency = 0

# Find the element(s) with the highest frequency
for i in tup:
    frequency = tup.count(i)

    if frequency > maximum_frequency:
        maximum_frequency = frequency
        result.clear()
        result.append(i)

    elif frequency == maximum_frequency and i not in result:
        result.append(i)

# Display the mode(s)
if tup:
    print("Mode(s):", tuple(result))
else:
    print("Tuple is empty.")