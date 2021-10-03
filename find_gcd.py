#Euclid's Algorithm to find the GCD of two numbers

def euclid(n1, n2):
    if not n1:
        return n2
    if not n2:
        return n1
    if n1 > n2:
        return euclid(n1 % n2, n2)
    else:
        return euclid(n2 % n1, n1)


if __name__ == "__main__":
    n1 = int(input())
    n2 = int(input())

    print("The GCD of the numbers is " + str(euclid(n1, n2)))
