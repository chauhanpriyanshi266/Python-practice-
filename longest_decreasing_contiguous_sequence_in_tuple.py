# Program to find the longest decreasing contiguous sequence in a tuple

tup = tuple(map(int, input("Enter elements: ").split()))

# Initialize the current and longest decreasing sequences
current_sequence = [tup[0]] if tup else []
longest_sequence = current_sequence.copy()

# Find the longest decreasing contiguous sequence
for i in range(1, len(tup)):
    if tup[i] < tup[i - 1]:
        current_sequence.append(tup[i])
    else:
        current_sequence = [tup[i]]

    # Update the longest sequence if the current one is longer
    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence.copy()

# Convert the result into a tuple
print("Longest decreasing contiguous sequence:", tuple(longest_sequence))