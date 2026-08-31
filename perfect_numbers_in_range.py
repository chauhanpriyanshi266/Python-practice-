# Program to find perfect numbers in a given range

a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Check every number from a to b
for i in range(a, b + 1):
    total = 0

    # Find the proper factors of i and calculate their sum
    for j in range(1, i):
        if i % j == 0:
            total += j

    # Check whether the sum of factors equals the number
    if total == i:
        print("Perfect number is:", i)
        print("Factors are:")

        # Print the factors of the perfect number
        for j in range(1, i):
            if i % j == 0:
                print(j, end=" ")