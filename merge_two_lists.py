# Program to merge two lists

l1 = []
l2 = []

n = int(input("Enter n: "))
m = int(input("Enter m: "))

# The loop runs n times for l1
for i in range(n):
    l1.append(int(input("Enter x: ")))

# The loop runs m times for l2
for i in range(m):
    l2.append(int(input("Enter y: ")))

print("Merged list:", l1 + l2)