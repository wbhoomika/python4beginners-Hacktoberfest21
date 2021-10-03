#Pronic number is a number which is the product of two consecutive integers, that is, a number n is a product of x and (x+1).


string=str(input())
s=[]
for i in string:
    s.append(i)
s.sort()
f=0
l=[]
for i in range(len(s)-1):
    if(int(s[i])<int(s[i+1])):
        x=int(s[i])*int(s[i+1])
        if (string.find(str(x))!=-1):
            f=1
            l.append(x)
l.sort()
if(f==0):
    print(-1)
else:
    for i in l:
        print(i,end=" ")