from random import randint


def run(die, rolls):
    for roll in range(rolls):  # Repeats the amount of print outs, based on the amount of rolls
        printStr = "Roll " + str(roll+1) + ": "
        for dice in range(die):  # Prints the amount of numbers desired
            printStr = printStr + " " + str(randint(1, 6))
        print(printStr)  # Prints the current roll's string


if __name__ == "__main__":
    die = int(input("How Many Dice? "))  # Gets the amount of Dice
    rolls = int(input("How many Rolls? "))  # Gets the amount of Rolls
    run(die, rolls)
