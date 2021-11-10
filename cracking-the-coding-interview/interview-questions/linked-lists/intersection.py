'''
#7
Given two singly linked lists, determine if the two lists intersect. Return the
interesecting node. Note that the intersection is defined based on reference,
not value. That is, if the kth node of the first linked list is the exact same
node (by reference) as the jth node of the second linked list, then they are
intersecting.

Example:
Input:
1 -> 2 -> 3 ->
				4 -> 5 -> 6 -> None
		  2 ->
Output:
4
'''

from singly_linked_list import LinkedList
from return_kth_to_last import kth_to_last

# Time Complexity O(N)
# Space Complexity O()
def intersection(list0: LinkedList, list1: LinkedList):
	list0_len = list0.get_size()
	list1_len = list1.get_size()
	
	# Get tail of both lists
	curr0 = list0.head
	while curr0:
		if curr0.next == None:
			tail0 = curr0
		curr0 = curr0.next
	
	curr1 = list1.head
	while curr1:
		if curr1.next == None:
			tail1 = curr1
		curr1 = curr1.next

	# Find longest LinkedList
	if list0_len > list1_len:
		long = list0
		short = list1.head
		adv = list0_len - list1_len
		long_len = list0_len - adv
	else:
		long = list1
		short = list0.head
		adv = list1 - list0
		long_len = list1_len - adv

	long = kth_to_last(long, long_len)
	
	while long and short:
		if long.data == short.data:
			return long.data
		# print(f'Long: {long.data}')
		# print(f'Short: {short.data}')
		long = long.next
		short = short.next

if __name__ == "__main__":
	link0 = LinkedList()
	link0.insert(1)
	link0.insert(2)
	link0.insert(3)
	link0.insert(4)
	link0.insert(5)
	link0.insert(6)

	link1 = LinkedList()
	link1.insert(2)
	link1.insert(4)
	link1.insert(5)
	link1.insert(6)

	print(intersection(link0, link1))