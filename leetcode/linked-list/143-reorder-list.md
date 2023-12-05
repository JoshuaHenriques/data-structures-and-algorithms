# Question Name
You are given the head of a singly linked-list. The list can be represented as:

```L0 → L1 → … → Ln - 1 → Ln```

Reorder the list to be on the following form:

```L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …```

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

*Example 1:*

```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

*Example 2:*

```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

*Constraints:*

```
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
```

## Naive Solution

### Approach
Using an array to help us create the new reordered linked list by using two pointers.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    nodes = []
    node = head.next
    while node:
        nodes.append(node.val)
        node = node.next

    l, r = 0, len(nodes) - 1
    curr = head
    
    while l <= r:
        node1 = ListNode(nodes[r])
        node2 = ListNode(nodes[l])

        curr.next = node1
        if l != r:
            curr.next.next = node2
        curr = curr.next.next
        l += 1
        r -= 1

    return head.next
```

## Optimized Solution

### Approach
Using a slow and fast pointer to pass through the linked list we're able to divide it into two portions. When the fast pointer reaches the end the slow pointer should be at the halfway point of the list. (If linked list is even the slow pointer will stop right before the start of the second portion so use slow.next and if it's odd then still use slow.next for the start so the second portion is smaller than the first) Take the second portion of the list and resverse it then we can read both portions and merge them together.

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```
def reorderList(self, head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
```