'''
#1
Write code to remove duplicated from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?

Examples: 
1 -> 4 -> 3 -> 5 -> 3 -> None
1 -> 4 -> 3 -> 5 -> None
'''

from collections import deque
from singly_linked_list import LinkedList

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

# Time Complexity: O(N)
# Space Complexity: O(N)
def remove_dups1(head: LinkedList):
    curr = head.head
    prev = head.head
    sett = set()
    sett.add(curr.data)
    while curr.next:
        prev = curr
        curr = curr.next
        if curr.data not in sett:
            sett.add(curr.data)
        else:
            prev.next = curr.next

if __name__ == "__main__":
    ll = deque([1, 4, 3, 5, 3])
    print(ll)
    print(remove_dups0(ll))

    link = LinkedList()
    link.insert(1)
    link.insert(4)
    link.insert(3)
    link.insert(5)
    link.insert(3)
    print(link.to_string())
    remove_dups1(link)
    print(link.to_string())

# Without using a buffer keeping constant space
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