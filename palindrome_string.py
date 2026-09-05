# Program to check whether a string is a palindrome

s = input("Enter string: ")

# Reverse the string
rev = s[::-1]

# Compare the original string with its reverse
if s == rev:
    print("Palindrome")
else:
    print("Not palindrome")