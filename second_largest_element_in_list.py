# Program to find the second largest element in a list

lst = []
n = int(input("Enter n: "))

# The loop runs n times
for i in range(n):
    lst.append(int(input("Enter x: ")))

lst.sort()

print("Second largest element:", lst[-2])