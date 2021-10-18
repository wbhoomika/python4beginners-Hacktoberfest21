T=int(input())
for i in range(T):
    n=list(map(int,input().split()))
    n1=set(n)
    if len(n1)==4:
        print(2)
    elif len(n1)==3:
        print(2)
    elif len(n1)==2:
        n.sort()
        n2=n[0]
        if(n.count(n2)==2):
            print(2)
        else:
            print(1)
    else:
        print(0)
