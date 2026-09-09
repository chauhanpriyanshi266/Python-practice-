# Program to reverse a list

lst = []
n = int(input("Enter n: "))

# The loop runs n times
for i in range(n):
    lst.append(int(input("Enter x: ")))

rev = []

for i in range(len(lst) - 1, -1, -1):
    rev.append(lst[i])

print("Reverse of the list is:", rev)