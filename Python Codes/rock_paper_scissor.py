import random
# This library helps make a random choice.
c = True
# Loop runs until this is true.
cu = ["r","p","s"]
# Stores the choices available for the computer
ps = 0
# This stores the player score.
cus = 0
# This stores the computer score.
while(c):  
    print("Enter r for \" ROCK \"")
    print("Enter p for \" PAPER \"")
    print("Enter s for \" SCISSOR \"")
    print("Enter w to reset")
    print("Enter q to quit the game")
    print("Player score = ",ps)
    print("Computer score = ",cus)
    # The current score gets printed.
    if(ps > cus):
        print("PLAYER Winning.")
    elif(cus > ps):
        print("COMPUTER Winning.")
    elif(ps == 0 and cus == 0):
        print("Let's Begin the Game!")
    else:
        print("It's a TIE!")
    # Comparing scores to determine the current winner.
    p_choice = input("Enter your choice ")
    # Inputting the choice
    for j in range(10000):
        print("\n")
    # This helps to clear the screen each time a move is made.
    c_choice = random.choice(cu)
    # This makes the random choice.
    print("Your Choice:\t",p_choice)
    if(p_choice=="r" or p_choice=="p" or p_choice=="s"):
        print("Computer chose:\t",c_choice)
        # This makes sure the statement is printed only when a valid moce is made.
    if (p_choice == "r" and c_choice == "p"):
        cus += 1
        print("Computer won.")
    elif (p_choice == "r" and c_choice == "s"):
        ps += 1
        print("Player won.")
    elif (p_choice == "p" and c_choice == "r"):
        ps += 1
        print("Player won.")
    elif (p_choice == "p" and c_choice == "s"):
        cus += 1
        print("Computer won.")
    elif (p_choice == "s" and c_choice == "p"):
        cus += 1
        print("Computer won.")
    elif (p_choice == "s" and c_choice == "r"):
        cus += 1
        print("Computer won.")
    # Incrementing the score whenever the computer wins and vice versa.
    elif (p_choice == c_choice):
        print("It's a Draw!")
    elif(p_choice == "w"):
        ps = 0
        cus = 0
    # This resets the scores.
    elif (p_choice == "q"):
        c = False
        # This ends the loop.
    else:
         print("Wrong input")
         # This handles invalid input.
print("Game Over")