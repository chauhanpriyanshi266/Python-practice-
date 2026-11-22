# Program to expand a run-length encoded tuple

n = int(input("Enter number of pairs: "))

pairs = []
result = []

# Take encoded pairs as input
for i in range(n):
    word = input("Enter word: ")

    frequency = int(input("Enter frequency: "))

    # Validate frequency
    while frequency < 0:
        print("Frequency cannot be negative.")
        frequency = int(input("Enter frequency again: "))

    pairs.append((word, frequency))

tup = tuple(pairs)

# Expand the run-length encoded tuple
for word, frequency in tup:
    for element in range(frequency):
        result.append(word)

# Display the expanded tuple
print("Expanded tuple:", tuple(result))