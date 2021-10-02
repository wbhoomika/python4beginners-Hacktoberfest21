# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 18:26:48 2021

@author: Debanjan Rudra
"""

def rearrange(A, n):

    A.sort()
 
    i, j = 1, 1
 
    while j < n:
    
        if A[j] > 0:
        
            break
        
        j += 1

    while (A[i] < 0) and (j < n):

        A[i], A[j] = A[j], A[i]  

        i += 2     
        j += 1
     
    return A

if __name__=='__main__':
    
    for _ in range(int(input())):
    
        A = list(map(int,input().rstrip().split()))
 
        ans = rearrange(A, len(A))
        
        print(*ans)