# 35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

*Example 1:*

```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

*Example 2:*

```
Input: nums = [1,3,5,6], target = 2
Output: 1
```

*Example 3:*

```
Input: nums = [1,3,5,6], target = 7
Output: 4
```

*Constraints:*

* 1 <= nums.length <= 104
* -104 <= nums[i] <= 104
* nums contains distinct values sorted in ascending order.
* -104 <= target <= 104

## Solution

### Approach

Use binary search to try to find the target and return it's index if found. If the target isn't found then the left pointer will always be where it would be inserted since the while loop terminates after l > r.

### Complexity

$$Time: O(logn)$$

$$Space: O(1)$$

### Code

```py
def searchInsert(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        # mid = (l + r) // 2
        mid = l + (r - l) // 2 # prevent overflow

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return l
```