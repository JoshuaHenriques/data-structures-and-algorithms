'''
#6
Implement a function to check if a linked list is a palindrome

Example:
Input: r -> a -> c -> e -> c -> a -> r -> None
Output: True
'''

from singly_linked_list import LinkedList

# Time Complexity O(N)
# Space Complexity O(N)
def palindrome(list: LinkedList) -> bool:
	if length() == 0 or length() == 1:
		return True
	# Copy list
	rev_list = LinkedList()
	curr = list.head
	while curr:
		rev_list.insert(curr.data)
		curr = curr.next
	# Reverse LinkedList
	prev = rev_list.reverse()
	curr = list.head
	while prev and curr:
		print(f'Prev = {prev.data}')
		print(f'Curr = {curr.data}')
		if prev.data != curr.data:
			return False
		prev = prev.next
		curr = curr.next
	return True

# Time Complexity O(N)
# Time Complexity O(1)
# https://quastor.org/cracking-the-coding-interview/linked-lists/palindrome
# def palindrome1(list: LinkedList) -> bool:
# 	length = list.get_size()
# 	if length == 0 or length == 1:
# 		return True
# 	if length % 2 == 0:
# 		half = length // 2
# 	elif length % 2 == 1:
# 		half = length // 2 + 1
	
# 	curr = list.head
# 	for _ in range(half):
# 		curr = curr.next
	
# 	second_half = curr.next
# 	curr.next = None
# 	second_half = LinkedList

if __name__ == "__main__":
	link = LinkedList()
	link.insert('r')
	link.insert('a')
	link.insert('c')
	link.insert('e')
	link.insert('c')
	link.insert('a')
	link.insert('r')

	print(palindrome(link))