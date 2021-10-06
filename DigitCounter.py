a = int(input("Enter a number: "))
digit =0
while a >0:
    a =a//10
    digit+=1
print("the number of digit of the entered number is : "+ str(digit))