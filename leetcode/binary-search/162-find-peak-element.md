# 162. Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

*Example 1:*

```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

*Example 2:*

```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
```

*Constraints:*

* 1 <= nums.length <= 1000
* -231 <= nums[i] <= 231 - 1
* nums[i] != nums[i + 1] for all valid i.

## Solution

### Approach

In every iteration of our binary search algorithm we check if nums[mid] is a peak element. If not we check if nums[mid] is less than nums[mid + 1] because if this condition is always met then the last element will always be a peak element since we know out of bounds elements are always less. 

### Complexity

$$Time: O(logn)$$

$$Space: O(1)$$

### Code

```py
def findPeakElement(self, nums: List[int]) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid] < nums[mid + 1]:
            l = mid + 1
        else:
            r = mid - 1

    return l
```
