# Program to find the maximum element in a list

lst = []
n = int(input("Enter n: "))

# The loop runs n times
for i in range(n):
    lst.append(int(input("Enter x: ")))

print("Maximum =", max(lst))