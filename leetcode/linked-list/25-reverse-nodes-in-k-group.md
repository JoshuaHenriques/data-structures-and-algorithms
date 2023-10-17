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
We create a healper function to get the kth node from a node. `groupPrev` is to keep track of the node before the start of a k-group, `groupPrev.next` would be the start of a k-group. `groupNext` to keep track of the node right after the group. While True, until we get to the last group in the linked list and it's not big enough to group reverse it. We call our getKth helper function to get the kth node passing in groupPrev. We now reverse the group as usual however we don't set prev to None because it will break our linked list so we set it to the groupNext node. The reverse ends when curr equals the end of the group, groupNext. Now we have to connect that reversed group properly by setting it to the node that keeps track of right before the start of the group so we assign `groupPrev.next` to the kth node. and set the old start node of that group as the new `groupPrev` since that is now the node right before the start of another group.

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
        prev = groupNext
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