'''
#4
Write code to partition a linked list around a value x, such that all nodes less
than x come before all nodes greater than or equal to x. If x is contained
within the list, the values of x only need to be after the elements less than x
(see below). The partition element x can appear anywere in the "right
partition"; it does not need to appear between the left and right partitions.

Example:
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

3, 24
'''
from singly_linked_list import LinkedList

# Time Complexity O(N)
# Space Complexity O(N)
def partition(list: LinkedList, target: int) -> LinkedList:
    lessThan = LinkedList()
    greaterThan = LinkedList()
    curr = list.head
    while curr:
        if curr.data < target:
            lessThan.insert(curr.data)
        else:
            greaterThan.insert(curr.data)
        curr = curr.next
    curr = lessThan.head
    while curr.next:
        curr = curr.next
    curr.next = greaterThan.head
    return lessThan
    
if __name__ == "__main__":
    link = LinkedList()
    link.insert(5)
    link.insert(6)
    link.insert(3)
    link.insert(5)
    link.insert(4)
    link.insert(10)
    print(link.to_string())
    print(partition(link, 4).to_string())
    