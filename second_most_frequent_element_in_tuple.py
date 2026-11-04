# Program to find the second most frequent element in a tuple

tup = tuple(map(int, input("Enter elements: ").split()))

highest_frequency = 0
highest_element = None

second_highest_frequency = 0
second_highest_element = None

# Find the highest and second-highest distinct frequencies
for i in tup:
    frequency = tup.count(i)

    # Update the highest frequency
    if frequency > highest_frequency:
        second_highest_frequency = highest_frequency
        second_highest_element = highest_element

        highest_frequency = frequency
        highest_element = i

    # Update the second-highest frequency
    elif frequency < highest_frequency and frequency > second_highest_frequency:
        second_highest_frequency = frequency
        second_highest_element = i

# Display the result
if second_highest_element is not None:
    print("Second most frequent element:", second_highest_element)
    print("Second highest frequency:", second_highest_frequency)
else:
    print("Second most frequent element does not exist.")