import requests
import json

print("                Welcome to My Dictionary")
print("                ------------------------")
print("\n ")
terminate = 0

def findMeaning(word):
    API_URL = r"https://api.dictionaryapi.dev/api/v2/entries/en/"+word
    meaning = requests.get(API_URL)
    #print(meaning.status_code)
    if meaning.status_code != 200:
        print("Word not found!")
        return
    word = (meaning.json())[0]
    m = (word['meanings'])[0]
    definition = m['definitions'][0]
    print(definition['definition'],"\n")


while not terminate:
    word = input("Enter the word: ")
    if not word:
        print("Please enter a valid word.")
        continue
    findMeaning(word)
    terminate = input("Hit Enter to continue or type E to exit: ")

print("\n ")
print("         THANK YOU FOR USING MY DICTIONARY")