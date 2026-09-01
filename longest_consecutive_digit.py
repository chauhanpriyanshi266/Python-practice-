# Program to find the longest consecutive digit

n = input("Enter number: ")

max_digit = n[0]
max_count = 1
current_count = 1

# Check each digit with the previous digit
for i in range(1, len(n)):
    if n[i - 1] == n[i]:
        current_count += 1
    else:
        current_count = 1

    # Update the longest consecutive digit
    if current_count > max_count:
        max_count = current_count
        max_digit = n[i]

print("Longest consecutive length:", max_count)
print("Digit:", max_digit)