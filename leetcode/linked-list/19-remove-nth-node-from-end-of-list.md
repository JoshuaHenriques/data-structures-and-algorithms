# 19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

*Example 1:*

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

*Example 2:*

```
Input: head = [1], n = 1
Output: []
```

*Example 3:*

```
Input: head = [1,2], n = 1
Output: [1]
```

*Constraints:*

```
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
```

## Naive Solution

### Approach
Two passthroughs. One to count the linked list, the second to find the nth node from the end, when found we assign the prev.next to the curr.next but if the target node is in the beginning we can just do head = curr.next

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    curr = head
    cnt = 0

    while curr:
        cnt += 1
        curr = curr.next

    i = 0
    curr = head
    prev = None
    while curr:
        if i == cnt - n:
            if i == 0:
                head = curr.next
                return head

            prev.next = curr.next
            return head
        
        prev = curr
        curr = curr.next
        i += 1
    
    return head
```

## Optimized Solution

### Approach
Using two pointers and a dummy node we can set the left pointer to dummy and right to head. Increment the right pointer n times so the distance between left and right is n. Then we can increment both pointers until right is null and the left pointer will be the node before the target node. From there we can remove the target node and return dummy.next (head)

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next

    return dummy.next
```