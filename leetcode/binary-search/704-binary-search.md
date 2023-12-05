# 704. Binary Search
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

*Example 1:*

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

*Example 2:*

```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

```

*Constraints:*

```
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
```

## Solution

### Approach
Using binary search we compare the target with the middle element in the sorted array and if its larger we then compare it to the middle from the old middle to the end of the array or if it's less it's from zero to the old middle. 

### Complexity
$$Time: O(logn)$$

$$Space: O(1)$$

### Code
```
def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    m = r // 2

    while l <= r:
        if target == nums[m]:
            return m
        elif target < nums[m]:
            r = m - 1
            m = r // 2
        elif target > nums[m]:
            l = m + 1
            m = (l + r) // 2

    return -1
```

## Optimized Solution

### Approach
Using binary search we compare the target with the middle element in the sorted array and if its larger we then compare it to the middle from the old middle to the end of the array or if it's less it's from zero to the old middle. 

### Complexity
$$Time: O(logn)$$

$$Space: O(1)$$

### Code
```
def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1
```