# Program to find duplicate elements in a list

lst = []
result = []

n = int(input("Enter n: "))

# The loop runs n times
for i in range(n):
    x = int(input("Enter x: "))
    lst.append(x)

# Find elements that occur more than once
for i in lst:
    if lst.count(i) > 1 and i not in result:
        result.append(i)

print("Duplicate elements:", result)