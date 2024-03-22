# 148. Sort List
Given the head of a linked list, return the list after sorting it in ascending order.

*Example 1:*

```
Input: head = [4,2,1,3]
Output: [1,2,3,4]
```

*Example 2:*

```
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

*Example 3:*

```
Input: head = []
Output: []
```

*Constraints:*

* The number of nodes in the list is in the range [0, 5 * 104].
* -105 <= Node.val <= 105

## Solution

### Approach
Using merge sort on the linked list using recursion. Split the list into two halfs by getting the middle node (using fast and slow pointer technique). Sort both the left and right list and return the recursive call. 

### Complexity
$$Time: O(nlogn)$$

$$Space: O(n)$$

### Code
```py
def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    # split the list into two halfs
    left = head
    right = self.getMid(head)
    tmp = right.next
    right.next = None
    right = tmp

    left = self.sortList(left)
    right = self.sortList(right)

    return self.merge(left, right)

def getMid(self, head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(self, list1, list2):
    tail = dummy = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    if list2:
        tail.next = list2

    return dummy.next
```
