# Program to remove duplicate characters from a string

s = input("Enter string: ")
result = ""

# Check whether the character is already in result
for ch in s:
    if ch not in result:
        result += ch

print(result)