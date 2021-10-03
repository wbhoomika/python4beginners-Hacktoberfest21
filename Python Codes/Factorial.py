#Program to return a factorial of a number
import sys

def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)

if __name__ == '__main__':
    arg = sys.argv
    print(recur_factorial(int(arg[1])))
