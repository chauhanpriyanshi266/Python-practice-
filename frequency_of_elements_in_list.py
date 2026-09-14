# Program to find the frequency of each element in a list

lst = []
result = []

n = int(input("Enter n: "))

# The loop runs n times
for i in range(n):
    lst.append(int(input("Enter x: ")))

for i in lst:
    if i not in result:
        print(i, "->", lst.count(i))
        result.append(i)