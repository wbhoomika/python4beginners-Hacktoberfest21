import random
guess = input("Heads or tails? (enter 'heads' or 'tails'): ")
answer = random.randint(1,2)
if answer == 1:
    answer = "heads"
else:
    answer = "tails"
if guess == answer:
    print("Nice!")
else:
    print("Sorry, thats wrong")
