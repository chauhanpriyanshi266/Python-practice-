# Program to reverse a string without using slicing

s = input("Enter string: ")
rev = ""

# Add each character to the beginning of rev
for ch in s:
    rev = ch + rev

print("Reverse of the string is :",rev)