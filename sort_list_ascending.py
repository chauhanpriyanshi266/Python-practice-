# Program to sort the elements of a list in ascending order

lst = []
n = int(input("Enter n: "))

# The loop runs n times
for i in range(n):
    lst.append(int(input("Enter x: ")))

lst.sort()

print("Sorted list:", lst)