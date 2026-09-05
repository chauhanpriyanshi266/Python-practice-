# Program to count the frequency of a character in a string

s = input("Enter string: ")
ch = input("Enter character: ")

count = 0

# Check each character in the string
for c in s:
    if c == ch:
        count += 1

print("Frequency of", ch, "is:", count)