# Program to find the longest repeating substring

s = input("Enter string: ")
longest = ""

for i in range(len(s)):
    add = ""

    for j in range(i, len(s)):
        add += s[j]
        count = 0

        # Count how many times 
            if s[k:k + len(add)] == add:
                count += 1

        # Update the longest repeating substring
        if count >= 2 and len(add) > len(longest):
            longest = add

if longest == "":
    print("Longest repeating substring:", -1)
else:
    print("Longest repeating substring:", longest)