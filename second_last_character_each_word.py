# Program to print the second-last character of each word

s = input("Enter string: ")
words = s.split()

for word in words:
    if len(word) >= 2:
        print(word[-2])