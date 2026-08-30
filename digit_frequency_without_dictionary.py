# Program to count the frequency of each digit without using a dictionary

n = input("Enter number: ")
printed = ""

# Check each digit of the number
for i in range(len(n)):

    # Skip the digit if its frequency has already been counted
    if n[i] in printed:
        continue

    count = 0

    # Count the frequency of the current digit
    for digit in n:
        if digit == n[i]:
            count += 1

    print(n[i], "->", count)

    # Store the digit so it is not counted again
    printed += n[i]