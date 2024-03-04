# 234. Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

*Example 1:*

```
Input: head = [1,2,2,1]
Output: true
```

*Example 2:*

```
Input: head = [1,2]
Output: false
```

*Constraints:*

* The number of nodes in the list is in the range [1, 105].
* 0 <= Node.val <= 9

## Naive Solution

### Approach
Convert linked list to an array, check if array is palindrome.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```py
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    arr = []

    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next

    left, right = 0, len(arr) - 1
    while left <= right:
        if arr[left] != arr[right]:
            return False

        left += 1
        right -= 1

    return True
```

## Optimized Solution

### Approach
Fast and slow pointer technique to find the midpoint of the linked list. Reverse the second half of the list and then check the first half with the nodes of the reversed second half.

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```py
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    # finding midpoint
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reversing the second half
    prev, curr = None, slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # checking if it's palindrome
    first_half, reversed_half = head, prev
    while first_half and reversed_half:
        if first_half.val != reversed_half.val:
            return False

        first_half = first_half.next
        reversed_half = reversed_half.next

    return True
```
