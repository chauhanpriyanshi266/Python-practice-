# Program to check whether two strings are anagrams or not

s = input("Enter string: ")
s1 = input("Enter string: ")

flag = True

# Check whether both strings have the same length
if len(s) != len(s1):
    flag = False
else:
    # Check the frequency of each character in both strings
    for ch in s:
        if s.count(ch) != s1.count(ch):
            flag = False
            break

# Display the result
if flag:
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")