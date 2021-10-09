import random
import string

ic = ['a', 'i', 'o', 'u', 'e']
Vowels = "aeiou"
yeaboi = "".join(set(string.ascii_letters) - set(Vowels))
starters = "abcdfghklmnprst"

#print (random.choice(yeaboi)+random.choice(ic)+random.choice(yeaboi)+random.choice(ic)+random.choice(ic)+random.choice(yeaboi))

word = []
n = int(input("how letters word do you want?"))

for i in range(0, n):
    if i == 1 :
        word.append(random.choice(starters))
    elif i % 2 == 0:
        word.append(random.choice(Vowels))
    else:
        word.append(random.choice(yeaboi))


str1 = ""  
for ele in word:  
    str1 += ele
        
 

print(str1)
    
    