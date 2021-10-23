def merge(arr1, arr2, n1, n2):
    arr3=[None]*(n1+n2)
    p1=0
    p2=0
    i=0
    while ( p1< n1 and p2 <n2):
        if (arr1[p1]<arr2[p2]):
            arr3[i]=arr1[p1]
            p1=p1+1
        else:
            arr3[i]=arr2[p2]
            p2=p2+1
        i=i+1

   
    while (p2<n2):
        arr3[i]=arr2[p2]
        p2=p2+1
        i=i+1
    while (p1<n1):
        arr3[i]=arr1[p1]
        p1=p1+1
        i=i+1
    
    print("The merged sorted array is :")
    print (arr3)

l1=[]
n1 = int(input("Enter number of elements in first array: "))
print ("Enter elements of the first sorted array ")
for i in range(0, n1):
    ele = int(input())
    l1.append(ele) 

l2=[]
n2 = int(input("Enter number of elements in second array: "))
print ("Enter elements of the second sorted array ")
for i in range(0, n2):
    ele = int(input())
    l2.append(ele) 
print("The first sorted array is :")
print (l1)
print("The second sorted array is :")
print (l2)
merge(l1, l2,n1,n2)
