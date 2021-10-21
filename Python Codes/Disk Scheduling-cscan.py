n=int(input("enter number of requests:"))
head=int(input("enter the current head position(0-199):"))
pr=[]
seekTime=0
order=[]
print("enter the requests")
for i in range(n):
	value=int(input())
	pr.append(value)
pr.sort()

temp=0
index=0
temp=1000
for i in range(n):
    if(pr[i]>head and pr[i]<temp):
        temp=pr[i]
        index=i
temp=index
order.append(pr[temp])
seekTime+=abs(pr[temp]-head)
temp+=1
while(temp<n):
    order.append(pr[temp])
    seekTime+=abs(pr[temp]-pr[temp-1])
    temp+=1
order.append(199)
seekTime+=abs(pr[n-1]-199)
order.append(0)
seekTime+=abs(199-0)
temp=0
order.append(pr[temp])
seekTime+=abs(pr[temp]-0)
temp+=1
while(temp<index):
    order.append(pr[temp])
    seekTime+=abs(pr[temp]-pr[temp-1])
    temp+=1
print("seek Time = ",seekTime)
print("order of scheduling :\n")
print(head," ->",end=" ")
for i in order:
    print(i," ->",end=" ")
print("end\n")