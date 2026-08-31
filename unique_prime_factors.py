# Program to find unique prime factors of a number

n = int(input("Enter number: "))

print("Unique prime factors:")

# Check every possible factor of n
for i in range(2, n + 1):

    # Check whether i is a factor of n
    if n % i == 0:

        # Check whether i is prime
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=",")