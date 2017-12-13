isPrime=0
n=int(input("Enter Number to Check: "))
if n == 1 or n == 0:
    print(n,"Is Not Prime Number ")
else:
    for i in range(1,n+1):
        if n%i==0:
            isPrime+=1
    if (isPrime==2):
        print(n,"Is Prime Number")
    else:
        print(n,"Is Not Prime Number")
