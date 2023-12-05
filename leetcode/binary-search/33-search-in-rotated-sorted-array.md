# 33. Search in Rotated Sorted Array
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

*Example 1:*

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

*Example 2:*

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

*Example 3:*

```
Input: nums = [1], target = 0
Output: -1
```

*Constraints:*

```
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
```

## Solution

### Approach
If the middle value is greater than our l pointer value then we know we're in the left sorted portion and if not we're in the right sorted portion. If we're in the left portion check if target is greater than the middle value or if target is greater than the left pointer value we update our left pointer and the inverse if we're in the right sorted portion

### Complexity
$$Time: O(logn)$$

$$Space: O(1)$$

### Code
```
def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    res = -1

    while (l <= r):
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[l]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    
    return res        
```