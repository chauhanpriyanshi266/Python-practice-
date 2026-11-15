# Program to find the first element whose cumulative frequency reaches a given threshold

tup = tuple(map(int, input("Enter elements: ").split()))
threshold = int(input("Enter threshold: "))

cumulative_frequency = 0
result = None

# Calculate cumulative frequency
for i in tup:
    frequency = tup.count(i)

    # Count each distinct element only once
    if i not in tup[:tup.index(i)]:
        cumulative_frequency += frequency

        if cumulative_frequency >= threshold:
            result = i
            break

# Display the result
if result is not None:
    print("First element reaching the threshold:", result)
else:
    print("Threshold not reached.")