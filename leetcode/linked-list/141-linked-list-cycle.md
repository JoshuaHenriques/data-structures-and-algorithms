# 141. Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

*Example 1:*

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

*Example 2:*

```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

*Example 3:*

```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

*Constraints:*

```
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
```

## Naive Solution

### Approach
Since linked lists uses pointers to a node and not just values we can use a hashset to store the actual nodes and compare them against each other. So we check at each iteration if that node is already in the set, if true then we know we hit a cycle.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```py
def hasCycle(self, head: Optional[ListNode]) -> bool:
    hashset = set()

    while head:
        if head in hashset:
            return True
        
        hashset.add(head)
        head = head.next

    return False
```

## Optimized Solution

### Approach
Using the rabbit and tortoise idea we'll have two pointers and when we iterate we increment the pointer for one of them by 2 and if there's a cycle the two pointers will eventually end up at the same node.

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```py
# code
```