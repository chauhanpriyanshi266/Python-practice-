# Program to remove duplicates from a list

lst = []
result = []

n = int(input("Enter n: "))

# The loop runs n times
for i in range(n):
    lst.append(int(input("Enter x: ")))

for i in range(n):
    if lst[i] not in result:
        result.append(lst[i])

print("List after removing duplicates:", result)