def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i # start multiplying all the integers starting from 1 till the given number.
    return f
num=int(input("Enter an integer number"))
#I'm calling the calling function
print("The factorial of",num,"is",factorial(num))
