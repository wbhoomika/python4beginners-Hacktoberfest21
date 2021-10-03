#!/usr/bin/env python
# coding: utf-8

# In[1]:


def bubble_sort(arr):                               #Created a function named Bubble-sort
    for i in range(len(arr)-1):                     #Created a for loop for itterating through each element of the array
        for j in range(len(arr)-1):                 #Created again a for loop for itterating through the list
            if arr[j]>arr[j+1]:                     #Comparing the adjacent element 
                arr[j],arr[j+1]=arr[j+1],arr[j]     #Swapping the elements according to their values (Bigger / Smaller)
arr=[int(x) for x in input().split()]               #List comprehension for taking the input through user
bubble_sort(arr)                                    #Calling the function that we created
print(arr)                                          #As the list are mutable so calling the same array after applying the function

