from random import *

def generatePassword(length, specialChars):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "0123456789"
    specials = "!@#$%^&*()_-=+|}{[]\\';:/?><,."
    stringToUse = chars + nums
    password = ""
    if specialChars:
        stringToUse += specials
    
    
    for x in range(int(length)):
        rand = randint(1, len(stringToUse))
        password += stringToUse[rand]

    return password

print("Password Generator")

howLong = input("How long should the password be?\n")

specHolder = input("Do you want special characters? (y/n)\n")

if specHolder == "n":
    specialChars = False
else:
    specialChars = True

print(generatePassword(howLong, specialChars))