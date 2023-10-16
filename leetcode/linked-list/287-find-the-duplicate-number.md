# 287. Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

*Example 1:*

```
Input: nums = [1,3,4,2,2]
Output: 2
```

*Example 2:*

```
Input: nums = [3,1,3,4,2]
Output: 3
```

*Constraints:*

```
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
```

## Optimized Solution

### Approach
Visualize the array as linked list by having the elements be the index it's pointing at. index 0 points to index 1, index 1 points to index 3, index 3 points to index 2, index 2 points to index 4, index 4 points to index 2, and now a cycle is created. We use Floyd's tortoise and hares algorithm to find the first intersection, then start using two slow pointers until the second intersection which is the start of the cycle. 

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```
def findDuplicate(self, nums: List[int]) -> int:
    slow, fast = 0, 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow
```