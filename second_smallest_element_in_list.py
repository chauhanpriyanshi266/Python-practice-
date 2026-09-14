# Program to find the second smallest element in a list

lst = []
n = int(input("Enter n: "))

# The loop runs n times
for i in range(n):
    lst.append(int(input("Enter x: ")))

lst.sort()

print("Second smallest element:", lst[1])