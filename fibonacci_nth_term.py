# Program to find the nth term of the Fibonacci series
n = int(input("Enter number : "))
# The first and second fibonacci terms are 1
if(n == 1 or n == 2):
    print("Fibonacci of",n,"th term is :",1)
else:
    a = 1
    b = 1
    fibo_sum = 0
    # Calculate the Fibonacci terms from 3rd to nth
    for i in range(3,n+1):
        fibo_sum = a + b 
        # Move to the next two terms 
        a = b 
        b = fibo_sum
    print(" Fibonacci of",n,"th tern is :",fibo_sum)