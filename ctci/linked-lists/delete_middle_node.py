'''
#3
Implement an algorithm to delete a node in the middle (i.e., any node but the first
and last node, not necessarily the exact middle) of a singly linked list, given
only access to that node

Example:
Input: a - > b -> c -> d -> e -> f
Result: a -> b -> d -> e -> f
'''

from singly_linked_list import LinkedList, Node

# Time Complexity O(N)
# Space Complexity O(N)
def delete_middle_node(list: LinkedList) -> LinkedList:
    size = list.get_size()
    middle = (size - 1) // 2
    cnt = 0
    curr = list.head
    prev = list.head
    while curr.next:
        if cnt == middle:
            prev.next = curr.next
            break            
        cnt += 1
        prev = curr
        curr = curr.next
    return list

# https://quastor.org/cracking-the-coding-interview/linked-lists/delete-middle-node
def delete_node(node: Node):
    node.data = node.next.data
    node.next = node.next.next

if __name__ == "__main__":
   link = LinkedList()
   link.insert('a')
   link.insert('b') 
   link.insert('c') 
   link.insert('d') 
   link.insert('e') 
   link.insert('f')
   print(link.to_string())
   delete_middle_node(link)
   print(link.to_string()) 