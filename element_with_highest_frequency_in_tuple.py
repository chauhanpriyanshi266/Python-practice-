# Program to find the element with the highest frequency in a tuple

tup = tuple(map(int, input("Enter elements: ").split()))

highest_frequency = 0
highest_element = None

# Find the element with the maximum frequency
for i in tup:
    frequency = tup.count(i)

    if frequency > highest_frequency:
        highest_frequency = frequency
        highest_element = i

# Display the element and its frequency
if highest_element is not None:
    print("Element with highest frequency:", highest_element)
    print("Highest frequency:", highest_frequency)
else:
    print("The tuple is empty.")