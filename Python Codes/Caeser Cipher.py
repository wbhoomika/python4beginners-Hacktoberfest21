s=input("Enter a string:\n")
n=int(input("\nEnter the no. of rotations:\n"))
n=n%26
p=""

for i in s:
    if i.isupper():
        x=ord(i)+n
        if x not in range(65,91):
            x=64+(x-90)
        x=chr(x)
        p=p+x
    elif i.islower():
        x = ord(i) + n
        if x not in range(97, 123):
            x = 96 + (x - 122)
        x = chr(x)
        p = p + x
    else:
        p=p+i
print(p)
