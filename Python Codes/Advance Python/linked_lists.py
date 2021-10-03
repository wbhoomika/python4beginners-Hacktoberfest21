class Node:

	def __init__(self, data, next):
		self.data = data
		self.next = next

class LinkedList:

	def __init__(self):
		self.head = None

	def print(self):

		if self.head is None:
			print("Linked List is empty")
			return

		itr = self.head
		llstr = ' '

		while itr:
			llstr += str(itr.data) + '-->'
			itr = itr.next
		print(llstr)

	def get_length(self):

		count = 0
		itr = self.head

		while itr:
			count += 1
			itr = itr.next

		print(count)

	def insert_at_beginning(self, data):

		node = Node(data, self.head)
		self.head = node

	def insert_at_end(self, data):

		if self.head is None:
			self.head = Node(data, None)
			return

		itr = self.head

		while itr.next:
			itr = itr.next

		itr.next = Node(data, None)

	def insert_at(self, index, data):

		if index < 0 or index > self.get_length():
			raise Exception("Invalid Index")

		if index == 0:
			self.insert_at_beginning(data)
			return

		count = 0
		itr = self.head

		while itr:
			if count == index - 1:
				node = Node(data, itr.next)
				itr.next = node
				break

			itr = itr.next
			count += 1

	def remove_at(self, index):

		if index < 0 or index > self.get_length():
			raise Exception("Invalid Index")

		count = 0
		itr = self.head

		while itr:
			if count == index - 1:
				itr.next = itr.next.next
				break

			itr = itr.next
			count += 1

	def insert_values(self, data_list):

		self.head = None

		for data in data_list:
			self.insert_at_end(data)

if __name__ == '__main__':
	
	ll = LinkedList()

	
	print('''
		a -> insert values
		b -> insert a value at the beginning
		c -> insert a value at the end 
		d -> insert a value at any index
		e -> remove a value at any index
		f -> get the length of the linked list
		g -> exit from the program
		'''
		)

	while True:

		ch = input()

		if (ch == "a"):
			ll.insert_values(list(input().split()))
			ll.print()
			
		elif (ch == "b"):
			ll.insert_at_beginning(input())
			ll.print()
			
		elif (ch == "c"):
			ll.insert_at_end(input())
			ll.print()
			
		elif (ch == "d"):
			ll.insert_at(int(input()), input())
			ll.print()
			
		elif (ch == "e"):
			ll.remove_at(int(input()))
			ll.print()
			
		elif (ch == "f"):
			ll.get_length()
			
		elif(ch == "g"):
			break

