'''
#1
Write code to remove duplicated from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?

Examples: 
1 -> 4 -> 3 -> 5 -> 3 -> None
1 -> 4 -> 3 -> 5 -> None
'''

from collections import deque

# Time Complexity: O(N)
# Space Complexity: O(N)
def remove_dups0(ll: deque) -> deque:
    dict = {}
    new = deque()
    for i, node in enumerate(ll):
        dict[node] = i
    for node in dict:
        new.append(node)
    return new

# Without using a buffer
# Time Complexity: O(N^2)
# Space Complexity: O(1)
# def remove_dups1(ll: deque) -> deque:
#     remove = []
#     for node0 in ll:
#         for i, node1 in enumerate(ll, 1):
#             if node0 == node1:
#                 remove.append(node1)
#     print(remove)
#     for dup in remove:
#         ll.remove(dup)

# def remove_dups2(head):
# 	if head is None:
# 		return head 
# 	settes = set()
# 	settes.add(head.val)
# 	curr = head
# 	while curr and curr.next:
# 		if curr.next.val in settes:
# 			curr.next = curr.next.next
# 		else:
# 			settes.add(curr.next.val)
# 			curr = curr.next
# 	return head

if __name__ == "__main__":
	ll = deque([1, 4, 3, 5, 3])
	print(ll)
	print(remove_dups0(ll))
