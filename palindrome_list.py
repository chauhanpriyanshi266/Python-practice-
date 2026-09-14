# Program to check whether a list is a palindrome

lst = []
rev = []

n = int(input("Enter n: "))

# The loop runs n times for the list
for i in range(n):
    lst.append(int(input("Enter element: ")))

# Create the reversed list
for i in range(len(lst) - 1, -1, -1):
    rev.append(lst[i])

# Compare the original and reversed lists
if rev == lst:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")