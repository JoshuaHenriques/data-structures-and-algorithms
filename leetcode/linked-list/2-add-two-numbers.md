# Question Name
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

*Example 1:*

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

*Example 2:*

```
Input: l1 = [0], l2 = [0]
Output: [0]
```

*Example 3:*

```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

*Constraints:*

```
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
```

## Naive Solution

### Approach
Multiple pass throughsConvert both linked lists to arrays then integers, add them together, and convert the sum into an array then convert that to a linked list

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    curr1 = l1
    curr2 = l2
    l1Num = ""
    l2Num = ""
    res = []

    while curr1:
        l1Num += f'{curr1.val}'
        curr1 = curr1.next

    while curr2:
        l2Num += f'{curr2.val}'
        curr2 = curr2.next

    res = int(l1Num[::-1]) + int(l2Num[::-1])
    res = [int(num) for num in str(res)]

    resHead = ListNode(0)
    resCurr = resHead
    for i in range(len(res) - 1, -1, -1):
        resCurr.val = res[i]
        if i > 0:
            resCurr.next = ListNode(0)
            resCurr = resCurr.next

    return resHead
```

## Optimized Solution

### Approach
One pass through. Visually think of the problem as a traditional addition problem where one number is above the other and the summation is below the line. We add the number from the 1's place first and put any carries on top the the next number in the 10s place. We implement this same process and use the fact that the input lists are in reverse order helps us simple pass through both lists regularly. Just remember to add the carry even if both lists are empty.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        val = val1 + val2 + carry
        carry = val // 10
        num = val % 10

        curr.next = ListNode(num)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next
```