# 34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

*Example 1:*

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

*Example 2:*

```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

*Example 3:*

```
Input: nums = [], target = 0
Output: [-1,-1]
```

*Constraints:*

* 0 <= nums.length <= 105
* -109 <= nums[i] <= 109
* nums is a non-decreasing array.
* -109 <= target <= 109


## Solution

### Approach

Perform binary search to find the target. If we do we create another two pointers and have one of them scan the left side and the other scan the right side until we're out of bounds or we stop seeing the target element. We also update the result each iteration.

### Complexity

$$Time: O(n)$$

$$Space: O(1)$$

### Code

```py
def searchRange(self, nums: List[int], target: int) -> List[int]:
    res = [-1, -1]
    l, r = 0, len(nums)

    while l <= r:
        mid = l + (r - l) // 2
        
        if mid >= len(nums):
            return res

        if nums[mid] == target:
            res[0], res[1] = mid, mid
            pl, pr = mid - 1, mid + 1

            while pl >= 0 and nums[pl] == target:
                res[0] = pl
                pl -= 1

            while pr < len(nums) and nums[pr] == target:
                res[1] = pr
                pr += 1
                
            return res
        elif nums[mid] < target:
            l = mid + 1
        else: 
            r = mid - 1

    return res
```