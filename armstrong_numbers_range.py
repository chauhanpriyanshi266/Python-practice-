# Program to find Armstrong numbers in a given range

n = int(input("Enter number : "))
print("Armstrong numbers are : ")

# Check every number from 1 to n
for i in range(1, n + 1):
    digit_sum = 0
    num = str(i)

    # Calculate the sum of digits raised to the number of digits
    for j in range(len(num)):
        digit_sum += int(num[j]) ** len(num)

    # Check whether the calculated value equals the original number
    if digit_sum == i:
        print(i)