# 206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

*Example 1:*

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

*Example 2:*

```
Input: head = [1,2]
Output: [2,1]
```

*Example 3:*

```
Input: head = []
Output: []
```

*Constraints:*

```
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
```

## Naive Solution

### Approach
Iterate through the list to assign values to a list, reverse the list and create another linked list that's reversed.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    arr = []
    newHead = head

    while newHead:
        arr.append(newHead.val)
        newHead = newHead.next

    arr.reverse()

    headp = head
    for i in range(len(arr)):
        head.val = arr[i]
        head = head.next

    return headp
```

## Optimized Iterative Solution

### Approach
Using two pointers, prev and curr, we can first store curr.next to a temp variable so we can have curr.next point to prev and have prev point to curr then we can assign curr to next. Doing this swaps properly swaps what the pointers are pointing at to reverse the linked list in one pass through 

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev
```

## Optimized Recursive Solution

### Approach
Base case is if head is null since we're doing recursion. Keep track of the new head returned by the recursive call with newHead. If there is a head.next set that node's next to the old head and set that head.next to null

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    newHead = head
    if head.next:
        newHead = self.reverseList(head.next)
        head.next.next = head
    head.next = None

    return newHead
```