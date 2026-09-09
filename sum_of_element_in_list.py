# Program to find the sum of the elements in a list

lst = []
n = int(input("Enter n: "))

# The loop runs n times
for i in range(n):
    lst.append(int(input("Enter x: ")))

total = 0

for i in range(n):
    total += lst[i]

print("Sum of the elements of the list is:", total)