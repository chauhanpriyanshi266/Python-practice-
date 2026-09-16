# Program to find the minimum and maximum elements in a list without using min() and max()

lst = []
n = int(input("Enter n: "))

# The loop runs n times
for i in range(n):
    x = int(input("Enter x: "))
    lst.append(x)

maximum = lst[0]
minimum = lst[0]

# Compare each element with the current minimum and maximum
for i in lst:
    if i > maximum:
        maximum = i

    if i < minimum:
        minimum = i

print("List:", lst)
print("Maximum:", maximum)
print("Minimum:", minimum)