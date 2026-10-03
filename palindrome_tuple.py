# Program to check whether a tuple is a palindrome or not

tup = tuple(input("Enter elements: "))

rev = ()

# Create the reverse of the tuple
for i in range(len(tup) - 1, -1, -1):
    rev = rev + (tup[i],)

# Check whether the tuple is equal to its reverse
if tup == rev:
    print("The tuple is a palindrome.")
else:
    print("The tuple is not a palindrome.")