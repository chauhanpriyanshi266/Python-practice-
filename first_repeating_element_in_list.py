# Program to find the first repeating element in a list

n = int(input("Enter number of elements: "))
lst = []
# Input the elements of the list
for i in range(n):
    x = int(input("Enter element: "))
    lst.append(x)

result = []

# Check the frequency of each element
for i in range(len(lst)):
    count = 0
    for j in range(len(lst)):
        if lst[i] == lst[j]:
            count += 1
    # Store the first element that occurs more than once
    if count > 1:
        result.append(lst[i])
        break

print("First repeating element:", result)