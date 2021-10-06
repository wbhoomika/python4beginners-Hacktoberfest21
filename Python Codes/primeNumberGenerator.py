def primeChecker(start, stop):
    k = 1
    for number in range(start, stop):
        if number == 1:
            print(str(number) + " is neither prime nor composite")
        else:
            for i in range(2, number):
                if number % i != 0:
                    k = 1
                elif number % i == 0:
                    k = k + 1
                    break
            if k == 1:
                print(str(number) + " is prime number")
            
start = int(input("enter the starting number: "))
stop = int(input("enter the stoping number: "))

primeChecker(start, stop)