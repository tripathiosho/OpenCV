class Node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
	def __init__(self):
		self.head = None
		
	def insert_at_begining(self,data):
		node = Node(data, self.head)
		self.head = node
	
	def print_ll(self):
		if self.head is None:
			print("LL is empty")
			return 
		itr = self.head
		llstr = ''
		while itr:
			llstr += str(itr.data) + '---->'
			itr = itr.next

if __name__ == '__main__':
	ll= LinkedList()
	ll.insert_at_begining(5)
	ll.insert_at_begining(89)
	ll.print_ll()
