# Program to move all even numbers before odd numbers in a list

lst = []

n = int(input("Enter number of elements: "))

# Input the elements of the list
for i in range(n):
    x = int(input("Enter element: "))
    lst.append(x)

result = []

# Add all even numbers first
for i in lst:
    if i % 2 == 0:
        result.append(i)

# Add all odd numbers after the even numbers
for i in lst:
    if i % 2 != 0:
        result.append(i)

print("List after moving even numbers before odd numbers:", result)