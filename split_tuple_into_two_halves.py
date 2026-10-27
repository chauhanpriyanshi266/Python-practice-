# Program to split a tuple into two approximately equal halves
# without using a loop

tup = tuple(map(int, input("Enter elements: ").split()))

# Calculate the split position, giving the first half the extra element
mid = (len(tup) + 1) // 2

first = tup[:mid]
second = tup[mid:]

# Display both halves
print("First half:", first)
print("Second half:", second)