# 300. Longest Increasing Subsequence
Given an integer array nums, return the length of the longest strictly increasing
subsequence.

*Example 1:*

```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

*Example 2:*

```
Input: nums = [0,1,0,3,2,3]
Output: 4
```

*Example 3:*

```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

*Constraints:*

```
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
```

## Top Down Recursion Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def lengthOfLIS(self, nums: List[int]) -> int:
    lis = []
    result = 0

    def dfs(i, arr):
        nonlocal result
        if i >= len(nums):
            return
            
        if nums[i] > arr[-1]:
            arr.append(nums[i])
            result = max(result, len(arr) - 1)
            dfs(i + 1, arr.copy())
            arr.pop()

        dfs(i + 1, arr.copy())

    dfs(0, [float("-inf")])
    return result
```

## Optimized Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
# code
```