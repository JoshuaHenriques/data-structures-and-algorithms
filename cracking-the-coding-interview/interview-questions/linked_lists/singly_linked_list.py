class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
		
	def insert(self, data):
		node = Node(data)
		if self.head == None:
			self.head = node
			self.size += 1
			return
		curr = self.head
		while curr.next:
			curr = curr.next
		curr.next = node
		curr = node
		self.size += 1

	def delete(self, data):
		if self.head == None: return
		curr = self.head
		prev = self.head
		while curr.next:
			if curr.data == data:
				prev.next = curr.next
				self.size -= 1
				return
			prev = curr
			curr = curr.next

	def search(self, data):
		curr = self.head
		cnt = 0
		while curr.next and curr.data != data:
			cnt += 1
			curr = curr.next
		if curr.data == data: return cnt
		return -1

	def get(self, index):
		curr = self.head
		cnt = 0
		while curr.next and cnt != index:
			cnt += 1
			curr = curr.next
		if cnt == index: return curr.data
		return None


	def get_size(self):
		print(self.size)

	def to_string(self):
		curr = self.head
		while curr:
			print(curr.data, end=' -> ')
			curr = curr.next
		print('None')

if __name__ == "__main__":
	linked_list = LinkedList()
	linked_list.insert(5)
	linked_list.insert(6)
	linked_list.insert(4)
	linked_list.insert(7)
	linked_list.insert(8)
	linked_list.insert(19)
	linked_list.to_string()
	linked_list.get_size()
	linked_list.delete(6)
	linked_list.to_string()
	print(linked_list.search(8))
	print(linked_list.get(3))
	print(linked_list.search(19))