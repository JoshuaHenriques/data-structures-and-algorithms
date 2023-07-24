'''
#5
You have two numbers represented by a linked list, where each node contains a
single digit. The digits are stored in reverse order, such that the 1's digit is
at the head of the list. Write a function that adds the two numbers and returns
the sum as a linked list.

Example:
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). 617 + 295
Output: 2 -> 1 -> 9 

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem
'''

from singly_linked_list import LinkedList

# Time Complexity O(N)
# Space Complexity O(N)
def sum_lists(list0: LinkedList(), list1: LinkedList()) -> LinkedList():
    num0 = [None]*list0.get_size()
    num1 = [None]*list1.get_size()
    
    index = list0.get_size() - 1
    curr = list0.head
    while curr:
        num0[index] = curr.data
        index -= 1
        curr = curr.next
        
    curr = list1.head
    index = list1.get_size() - 1
    while curr:
        num1[index] = curr.data
        index -= 1
        curr = curr.next
    
    num00 = int(''.join(map(str, num0)))
    num11 = int(''.join(map(str, num1)))
    sum = num00 + num11
    
    sum_list = list(map(int, str(sum)))
    end = len(sum_list) - 1
    sum_link = LinkedList()
    for i in range(len(sum_list)):
        sum_link.insert(sum_list[end - i])
    return sum_link, sum

if __name__ == "__main__":
    link0 = LinkedList()
    link0.insert(7)
    link0.insert(1)
    link0.insert(6)
     
    link1 = LinkedList()
    link1.insert(5)
    link1.insert(9)
    link1.insert(2)
    
    sum_link, sum = sum_lists(link0, link1) 
    
    print(f'{sum_link.to_string()}. That is, {sum}')