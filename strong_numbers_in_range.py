# Program to find strong numbers in a given range

n = int(input("Enter number: "))

# Check every number from 1 to n
for i in range(1, n + 1):
    temp = i
    digit_sum = 0

    # Extract each digit of the number
    while temp > 0:
        digit = temp % 10
        fact = 1

        # Calculate the factorial of the digit
        for j in range(1, digit + 1):
            fact = fact * j

        # Add the factorial of the digit to the total
        digit_sum += fact
        temp //= 10

    # Check whether the sum of factorials equals the original number
    if digit_sum == i:
        print(i)