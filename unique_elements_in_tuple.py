# program to find the count of unique elememts in a tuple

tup = tuple(map(int,input("Enter elements : ").split()))
result = []
for i in tup:
    if i not in result:
        result.append(i)
print(tuple(result))
print(len(result))