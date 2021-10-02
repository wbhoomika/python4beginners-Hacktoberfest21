def checkPalindrome(x):
    t = x
    v = 0
    while t>0:
        r = t%10
        v = r + (v*10)
        t = int(t/10)
    if v==x:
        return 1

print("Enter a Number: ", end="")
n = int(input())

chk = checkPalindrome(n)
if chk==1:
    print("\n" + str(n) + " is a Palindrome Number")
else:
    print("\n" + str(n) + " is not a Palindrome Number")