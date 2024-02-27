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
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```py

```
