def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        p1=list1 #pointing to the head of list1
        p2=list2 #pointing to the head of list2
        dn=ListNode()  #made new node so that it will start to point the numbers of both lists in sorted order
        p3=dn #pointing to the head of new node called 'dn'
        while p1!=None and p2!=None:  #loop goes till head of either lists not reached to null node
            if p1.val < p2.val:  #compairing data of both the heads
                p3.next=p1 #the p3 will point the shortest head's data (here shortest is p1)
                p1=p1.next #move the p1 to the next node (after get pointed by p3 in previous step)
            else: 
                p3.next=p2  #the p3 will point the shortest head's data (here shortest is p2)
                p2=p2.next #move the p2 to the next node (after get pointed by p3 in previous step)
            p3=p3.next  #move the p3 to the next node (as from above conditions p3 will be pointing to either head of list1 or list2)
			
        if p1 != None:  #if p2 reached to null but list1 nodes still remaining to be accessed 
            p3.next=p1 #so p3 will point the remaining nodes of list1 
        if p2 != None:  #if p1 reached to null but list1 nodes still remaining to be accessed 
            p3.next=p2 #so p3 will point the remaining nodes of list2
        return dn.next #the last node will be the head of merging sorted lists (which is asked to be returned)
