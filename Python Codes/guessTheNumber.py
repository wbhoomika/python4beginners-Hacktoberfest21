import random
n = random.randint(1,100)
print('--------Welcome to the game--------')
print('Rules:')
print('1. Guess a number between 1 and 100')
print('2. We will tell you whether the number you chose is higher or lower than our number')
print('3. You win when you make the right guess within 10 attempts')

i = 0
k = False
for i in range(10):
    print("Have your guess:")
    x = int(input())
    if(x==n):
        k=True
        print(f'{x} is the correct guess. You won!!!')
        break
    elif(x>n):
        i+=1
        print('The number you guessed is higher than our number')
    else:
        i+=1
        print('The number you guessed is lower than our number')
    print(f'You have {10-i} chances remaining')
if(not k):
    print(f'Our number was: {n}')