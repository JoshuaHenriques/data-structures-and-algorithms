# 1004. Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

*Example 1:*

```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

*Example 2:*

```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

*Constraints:*
* 1 <= nums.length <= 105
* nums[i] is either 0 or 1.
* 0 <= k <= nums.length


## Naive Solution (TLE)

### Approach
Similar to below but here when we increment i we reset the right pointer to where i is and reset the k counter. Also recording the window size using longest isn't necessary and makes the solution confusing.

### Complexity
$$Time: O(n^2)$$

$$Space: O(1)$$

### Code
```py
def longestOnes(self, nums: List[int], k: int) -> int:
    i, j, x = 0, 1, k
    longest = 0

    while j < len(nums):
        if nums[j] == 0:
            k -= 1

            if k < 0:
                longest = max(longest, j - i - 1)
                i += 1
                j = i
                k = x
                        
        j += 1
    if k == 0:
        longest = max(longest, j - i - 1) 
    else:
        longest = max(longest, j - i) 
    return longest
```

## Optimized Solution

### Approach
Using two pointers to keep track of the window size. Iterate through array, if the right pointer is a 0 decrement k. If k < 0 we shift the whole window and increment k if the left pointer was a 0. After the loop we can return the size of the window.

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```py
def longestOnes(self, nums: List[int], k: int) -> int:
    i, j = 0, 0

    while j < len(nums):
        if nums[j] == 0:
            k -= 1

        if k < 0:
            if nums[i] == 0:
                k += 1
            i += 1
                        
        j += 1

    return j - i
```
