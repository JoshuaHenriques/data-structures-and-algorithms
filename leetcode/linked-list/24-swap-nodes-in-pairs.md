# 24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

*Example 1:*

```
Input: head = [1,2,3,4]
Output: [2,1,4,3]
```

*Example 2:*

```
Input: head = []
Output: []
```

*Example 3:*

```
Input: head = [1]
Output: [1]
```

*Constraints:*

* The number of nodes in the list is in the range [0, 100].
* 0 <= Node.val <= 100

## Solution

### Approach
Create a dummy node and set prev to dummy and curr as the head. We check that both curr and curr.next isn't None since we need to swap the pairs. Each iteration we save the next pair and the second node. Swap both node pointers, then we update the prev and curr pointers after.

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```py
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    prev, curr = dummy, head

    while curr and curr.next:
        nxtPair = curr.next.next
        second = curr.next

        second.next = curr
        curr.next = nxtPair
        prev.next = second

        prev = curr
        curr = nxtPair

    return dummy.next
```
