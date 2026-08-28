n = int(input("Enter number : "))
if(n == 1 or n == 2):
    print("Fibonacci of",n,"th term is :",1)
else:
    a = 1
    b = 1
    fibo_sum = 0
    for i in range(3,n+1):
        fibo_sum = a + b 
        a = b 
        b = fibo_sum
    print(" Fibonacci of",n,"th tern is :",fibo_sum)