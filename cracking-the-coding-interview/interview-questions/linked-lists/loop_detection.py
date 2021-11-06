'''
#8
Given a circular linked list, implement an algorithm that returns the node at
the beginning of the loop.

Definition
Circular linked list: a (corrupt) linked list in which a node's next pointer
points to an earlier node, so as to make a loop in the linked list.

Example:
Input: A -> B -> C -> D -> E -> C
Output: C
'''

from singly_linked_list import LinkedList

def loop_detection(list: LinkedList):
	dict = set()
	curr = list.head
	while curr:
		if curr.data in dict:
			return curr.data
		dict.add(curr.data)
		curr = curr.next
	return -1

if __name__ == "__main__":
	link = LinkedList()
	link.insert('A')
	link.insert('B')
	link.insert('C')
	link.insert('D')
	link.insert('E')
	link.insert('C')

	print(loop_detection(link))

