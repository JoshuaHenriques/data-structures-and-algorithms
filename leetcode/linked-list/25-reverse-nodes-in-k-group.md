# 25. Reverse Nodes in k-Group
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

*Example 1:*

```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

*Example 2:*

```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

*Constraints:*

```
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
```

## Naive Solution (Can't figure out how to convert array of nodes to a full linked list)

### Approach
Get the length of the linked list in one pass through. Create a loop at range length // k since that's how many groups we'll be reversing. Each iteration reverse each group and append it to an array to keep track of the groups, at the end append the remaining list nodes that aren't reversed. Trouble converting this array into a new linked list to get the solution.

### Complexity
$$Time: O(n*k)$$

$$Space: O(n)$$

### Code
```
def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    arr = []
    length = 0

    curr = head
    while curr:
        length += 1
        curr = curr.next

    curr = head
    for i in range(length // k):
        prev = None
        j = 0
        while curr:
            if j == k:
                break
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            j += 1
        
        arr.append(prev)
    arr.append(curr)

    if arr:
        head = arr[0]
        last = None
        
        for node in arr:
            curr = node
            while curr.next:
                curr = curr.next
            last = curr

        # head = arr[0]
        # curr = head
        # while curr.next:
        #     curr = curr.next
        
        # for i in range(1, len(arr)):
        #     curr.next = arr[i]
        #     while curr.next:
        #         curr = curr.next

    print(curr)                
    print(head)
    print(arr)
```

## Optimized Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    groupPrev = dummy

    while True:
        kth = self.getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next

        # reverse group
        prev = kth.next
        curr = groupPrev.next
        while curr != groupNext:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        temp = groupPrev.next
        groupPrev.next = kth
        groupPrev = temp
    return dummy.next



def getKth(self, curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr
```