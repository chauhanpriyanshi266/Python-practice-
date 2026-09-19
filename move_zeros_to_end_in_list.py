# Program to move all zeros to the end of a list

lst = []

n = int(input("Enter number of elements: "))

# Input the elements of the list
for i in range(n):
    x = int(input("Enter element: "))
    lst.append(x)

pos = 0

# Move all non-zero elements to the front
for i in range(len(lst)):
    if lst[i] == 0:
        continue

    lst[pos] = lst[i]
    pos += 1

# Fill the remaining positions with zeros
for i in range(pos, len(lst)):
    lst[i] = 0

print("List after moving zeros to the end:", lst)