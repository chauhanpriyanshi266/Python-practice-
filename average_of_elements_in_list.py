# Program to find the average of the elements in a list

lst = []
n = int(input("Enter n: "))

# The loop runs n times
for i in range(n):
    lst.append(int(input("Enter x: ")))

total = 0

for i in range(n):
    total += lst[i]

avg = total / n

print("Average of the elements of the list is:", avg)