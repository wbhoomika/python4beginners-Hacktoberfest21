# This is a game called Hi-Lo which accepts a number from 1 -100 and the user is given infinite amount of chances to guess it
# If the number is too high it will print "too high"
# If the number is too low it will print "too low"


from ast import Index
import random

print('''
                                                HI-LO GAME

INSTRUCTIONS

- Computer generates a secret number between 1 - 100
- User should guess that number with infinite number of chances
- If the number is too high from the secret number it prints "Too High"
- If the number is too low from the secret number it prints "Too Low"
- If you guess the number correctly you will exit the game

                                        SO WHAT ARE YOU WAITING FOR!!!!
                                            LET'S PLAY THE GAME

''')

# this function is used to prompt user to enter a user input
def userValue():
    userInputValue = int(input("Enter Your Guess : "))
    return userInputValue   

# this function is used to generate a random numner using the library random.
def randomNumberGenerator():
    computerValue = random.randint(1,100)
    return computerValue

# this is the main function
def main():
    user_value = userValue()
    computer_value = randomNumberGenerator()
    

    # this list is created in order to store and display the wrong guess done by the user.
    wrong_guesses = []

    # While loop is used to check if the user inputs the correct value.
    while user_value != computer_value:
        
        # if, elif, else conditions are used inorder to print the high, low or correct input
        if user_value > computer_value:
            print('Too High')
            user_value = userValue()
        elif user_value < computer_value:
            print('Too Low')
            user_value = userValue()

        # List is used to add the last wrong guess done by the user
        if user_value != computer_value:
            wrong_guesses.append(user_value)
            print(wrong_guesses)
    else:
        print('Well Done. You guessed it right')
    
    

# calling main function
if __name__ == "__main__":
    main()

