# 334. Increasing Triplet Subsequence
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

*Example 1:*

```
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
```

*Example 2:*

```
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
```

*Example 3:*

```
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
```

*Constraints:*
* 1 <= nums.length <= 5 * 105
* -231 <= nums[i] <= 231 - 1

## Solution

### Approach
Every iteration we reassign either s1 or s2 with the minimum value of itself and the current number. If we ever get a condition that's greater than s2 than we know there exists two smaller numbers before it even if s1 and s2 get overwritten since it was initialized as maxsize.:w


### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```py
def increasingTriplet(self, nums: List[int]) -> bool:
    s1 = s2 = float("inf")

    for x in nums:
        if x > s2:
            return True
        if x > s1:
            s2 = min(x, s2)
        s1 = min(x, s1)
    
    return False
```
