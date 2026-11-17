# Program to find the longest consecutive sequence in a tuple

tup = tuple(map(int, input("Enter elements: ").split()))

# Remove duplicate elements and sort them
unique = set(tup)
t = sorted(unique)

# Initialize the current and longest sequences
current_sequence = [t[0]] if t else []
longest_sequence = current_sequence.copy()

# Find the longest consecutive sequence
for i in range(1, len(t)):

    if t[i] == t[i - 1] + 1:
        current_sequence.append(t[i])

    else:
        current_sequence = [t[i]]

    # Update the longest sequence if a longer one is found
    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence.copy()

# Display the result
print("Longest consecutive sequence:", tuple(longest_sequence))