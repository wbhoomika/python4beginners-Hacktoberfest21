def isprime(n):
    f=2
    while f*f<n:
        if n%f == 0:
            return False
        f+=1
    return True

k = int(input("Enter number: "))
for i in range(k):
    if isprime(i):
        print(i
