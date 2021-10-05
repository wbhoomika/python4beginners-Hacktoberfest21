def fibonacci(n):#, I have used the function def Fibonacci
	fib = [1, 1]
	
	for i in range(2, n):
		fib.append(fib[i-1] + fib[i-2])

	return fib[-1]

n = int(input("Enter a number : "))

for i in range(n):
	print(fibonacci(i))
