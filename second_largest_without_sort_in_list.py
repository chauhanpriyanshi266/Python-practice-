# Program to find the second largest element without using sort()

lst = []

n = int(input("Enter number of elements: "))

# Input the elements of the list
for i in range(n):
    x = int(input("Enter element: "))
    lst.append(x)

largest = float("-inf")
second = float("-inf")

# Find the largest and second largest elements
for i in lst:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i < largest:
        second = i

print("Largest:", largest)
print("Second largest:", second)