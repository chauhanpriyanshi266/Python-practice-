# Program to find the even and odd elements from a list

lst = []
n = int(input("Enter n: "))

# The loop runs n times
for i in range(n):
    lst.append(int(input("Enter x: ")))

even = []
odd = []

for i in range(n):
    if lst[i] % 2 == 0:
        even.append(lst[i])
    else:
        odd.append(lst[i])

print("Even elements of the list are:", even)
print("Odd elements of the list are:", odd)