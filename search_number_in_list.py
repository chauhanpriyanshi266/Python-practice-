# Program to search for a given number in a list

lst = []
n = int(input("Enter n: "))

# The loop runs n times
for i in range(n):
    lst.append(int(input("Enter x: ")))

m = int(input("Enter the number to search: "))

for i in range(n):
    if lst[i] == m:
        print("Given number is in the list:", lst[i])
        break
else:
    print("Given number is not in the list")