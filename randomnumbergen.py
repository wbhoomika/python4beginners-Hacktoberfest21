from random import randint

def run(digits, numbers):
    for roll in range(numbers):  # Repeats the amount of print outs, based on the amount of rolls
        printStr = ""
        for num in range(digits):  # Prints the amount of numbers desired
            printStr = printStr + str(randint(0, 9))
        print(printStr)  # Prints the current number's string


if __name__ == "__main__":
    digits = int(input("How Many digits? "))  # Gets the amount of digits
    numbers = int(input("How many total numbers? "))  # Gets the amount of numbers to output
    run(digits, numbers)
