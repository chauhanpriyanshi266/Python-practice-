# Program to left rotate the elements of a list

lst = []
n = int(input("Enter n: "))

# The loop runs n times
for i in range(n):
    lst.append(int(input("Enter x: ")))

print("List =", lst)

l = lst[1:] + [lst[0]]

print("Left rotated list:", l)