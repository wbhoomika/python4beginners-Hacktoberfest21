#first let's import random procedures since we will be shuffling
import random

#next, let's start building list holders so we can place our cards in there:
cardfaces = []
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
royals = ["J", "Q", "K", "A"]
deck = []

#now, let's start using loops to add our content:
for i in range(2,11):
	cardfaces.append(str(i)) #this adds numbers 2-10 and converts them to string data
for j in range(4):
	cardfaces.append(royals[j]) #this will add the royal faces to the cardbase
for k in range(4):
	for l in range(13):
		card = (cardfaces[l] + " of " + suits[k])
		#this makes each card, cycling through suits, but first through faces
		deck.append(card)
		#this adds the information to the "full deck" we want to make
#now let's shuffle our deck!
random.shuffle(deck)
#now let's see the cards!
for m in range(52):
	print(deck[m])
  
  
#  output of the code 

# 3 of Diamonds
# A of Hearts
# 5 of Hearts
# 3 of Clubs
# 7 of Hearts
# J of Hearts
# 7 of Spades
# 2 of Clubs
# 2 of Spades
# 10 of Hearts
# K of Clubs
# K of Diamonds
# 7 of Diamonds
# J of Clubs
# 2 of Hearts
# Q of Hearts
# 6 of Spades
# K of Spades
# 10 of Clubs
# 4 of Diamonds
# A of Spades
# 9 of Hearts
# 9 of Diamonds
# 4 of Hearts
# 9 of Spades
# 5 of Diamonds
# K of Hearts
# J of Diamonds
# Q of Spades
# 8 of Diamonds
# 9 of Clubs
# 4 of Clubs
# 5 of Clubs
# 3 of Spades
# 8 of Clubs
# 4 of Spades
# 2 of Diamonds
# 8 of Hearts
# J of Spades
# 6 of Diamonds
# A of Clubs
# 10 of Diamonds
# 10 of Spades
# 6 of Hearts
# 5 of Spades
# A of Diamonds
# 7 of Clubs
# 3 of Hearts
# Q of Diamonds
# 6 of Clubs
# 8 of Spades
# Q of Clubs
