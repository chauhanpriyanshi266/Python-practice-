# Program to find the smallest positive missing integer from an unsorted tuple

tup = tuple(map(int, input("Enter elements: ").split()))

# Start checking from the smallest positive integer
num = 1

# Find the first positive integer missing from the tuple
while num in tup:
    num += 1

# Display the result
print("Smallest positive missing integer:", num)