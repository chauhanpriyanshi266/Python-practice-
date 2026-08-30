# Program to find prime numbers in a given range

a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Check every number between a and b
for i in range(a + 1, b):

    if i > 1:

        # Check whether i is divisible by any number from 2 to i-1
        for j in range(2, i):
            if i % j == 0:
                break

        # If no divisor is found, i is prime
        else:
            print(i)