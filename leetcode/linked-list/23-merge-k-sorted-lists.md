# 23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

*Example 1:*

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

*Example 2:*

```
Input: lists = []
Output: []
```

*Example 3:*

```
Input: lists = []
Output: []
```

*Constraints:*

```
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
```

## Naive Solution

### Approach
This solution will merge each linked list in the array one by one with the other

### Complexity
$$Time: O(n*k)$$

$$Space: O(n)$$

## Optimized Solution

### Approach
We take our lists and dividing them by two each iteration by merging two linked lists each time. Once we exhaust the list we'll have the new merged lists stored locally and we replace the main list with that and run the whole process over again until the main list length equals to 1.

### Complexity
$$Time: O(n*logk)$$

$$Space: O(n)$$

### Code
```
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        mergedLists = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if (i + 1) < len(lists) else None
            mergedLists.append(self.mergeList(l1, l2))
        lists = mergedLists
    return lists[0]

def mergeList(self, l1, l2):
    dummy = ListNode()
    node = dummy

    while l1 and l2:
        if l1.val < l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next

    if l1:
        node.next = l1
    else:
        node.next = l2

    return dummy.next
```