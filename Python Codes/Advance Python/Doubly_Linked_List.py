class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev, self.data, self.next = prev, data, next 

class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):
        itr = self.head
        self.head = Node(None, data, self.head)
        if itr != None:
            itr.prev = self.head

    def insert_at_end(self,data):
        if self.head == None:
            self.insert_at_beg(data)

        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(itr, data, None)

    def insert_at_pos(self,data,pos):
        itr = self.head
        node = Node(None,data,None)
        while pos-1:
            itr = itr.next
            pos -= 1
        node.prev = itr.prev
        node.next = itr
        itr.prev.next = node
        itr.prev = node 

    def delete_from_pos(self,pos):
        itr = self.head
        if pos == 1:
            itr = itr.next
            itr.prev = None
            self.head = itr
        else:
            while pos-1:
                itr = itr.next
                pos-=1
            itr.next.prev = itr.prev
            itr.prev.next= itr.next   

    def count_nodes(self):
        cnt = 1
        itr = self.head
        while itr.next:
            cnt +=1
            itr = itr.next
        return cnt

    def print(self):
        if self.head == None:
            print("list is empty")
        else:
            itr = self.head
            llstr = ""
            while itr:
                llstr += str(itr.data) + "<--->"
                itr = itr.next
            print(llstr)

    def print_reverse(self):
        if self.head == None:
            print("list is empty")
        else:
            itr = self.head
            while itr.next:
                itr = itr.next

            llstr = ""
            while itr:
                llstr += str(itr.data) + "<--->"
                itr = itr.prev
            print(llstr)


# #=======execution=========#
if __name__ == "__main__":
    ll = linkedlist()
    ll.insert_at_end("Hello")
    ll.print()
    ll.insert_at_end("World")
    ll.print()
    ll.insert_at_end("testing this")
    ll.print()
    ll.insert_at_beg("123")
    ll.print()
    ll.insert_at_beg("432")
    ll.print()
    ll.insert_at_pos("88",3)
    ll.print()
    ll.delete_from_pos(3)
    print("\n")
    print(f"Length of the list at this point is = {ll.count_nodes()}") 
    print("\n")

    print("list in normal order")
    ll.print()

    print("\n")
    print("list in reverse order")
    ll.print_reverse()