# 189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

*Example 1:*

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

*Example 2:*

```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```


*Constraints:*

* 1 <= nums.length <= 105
* -231 <= nums[i] <= 231 - 1
* 0 <= k <= 105


## Solution

### Approach

Reverse the array, then reverse from 0 to k, and then reverse back from k to the end. Reversing the array rearranges the elements closer to the rotated array and then reversing back the two sections (sectioned off by k) of the array to get the desired rotated array.

### Complexity

$$Time: O(n)$$

$$Space: O(1)$$

### Code

```py
def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)

    def reverse(i, j):
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)
```
