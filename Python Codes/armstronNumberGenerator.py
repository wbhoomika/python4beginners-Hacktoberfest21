"""armstrong number is an number such that the sum of the digits raised to the power of the number of digits is equal to the original number 
 Eg - 153 =1^3 +5^3 +3^3
            =1+125+9              (here the number of digits is 3 and therefore each digit is raised to the power 3 and )
            =153         """
start = int(input("Enter starting number : "))
stop = int(input("Enter ending number : "))
for number in range(start, stop):
    digit = 0  # to reset the digit variable for every number in the loop
    sum = 0  # to reset the sum of digits for every number in the loop
    temp = int(number)
    while temp > 0:
        temp = temp // 10
        digit += 1
    temp = int(number)
    while temp > 0:
        rem = temp % 10
        c = rem
        for i in range(1, digit):
            c = c * rem
        sum = sum + c
        temp = temp // 10
    if sum == number:
        print(str(number) + " is an armstrong number")
