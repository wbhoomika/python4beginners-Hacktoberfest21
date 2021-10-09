num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
if num1 <= num2:
    min = num1
else:
    min = num2

for i in range(1, min + 1):
    if num1 % i == 0 & num2 % i == 0:
        gcd = i

lcm = int(num1 * num2 / gcd)

print("The gcd and lcm of " + str(num1) + " and " + str(2) + " is " + str(gcd) + " and " + str(lcm) + " respectively")
