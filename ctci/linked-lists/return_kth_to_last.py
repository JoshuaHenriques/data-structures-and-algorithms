'''
#2 
Implement an algorithm to find the kth to last element of a singly linked
list.

Examples:
1 -> 4 -> 7 -> 5 -> 3 -> None, 2
5
'''

from singly_linked_list import LinkedList, Node

# Time Complexity: O(N)
# Space Complexity: O(N)
def kth_to_last(list: LinkedList, kth: int) -> Node:
	if not list or kth == 0:
		return LinkedList()
	cnt = 0
	kth = list.get_size() - kth
	curr = list.head
	new = LinkedList()
	while curr.next:
		if cnt == kth:
			return curr
		cnt += 1
		curr = curr.next
	return -1


if __name__ == "__main__":
    link = LinkedList()
    link.insert(1)
    link.insert(4)
    link.insert(7)
    link.insert(5)
    link.insert(3)

    print(kth_to_last(link, 3).data)