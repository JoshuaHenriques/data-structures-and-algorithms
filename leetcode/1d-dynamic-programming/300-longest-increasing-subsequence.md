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
    def dfs(i):
        if i >= len(nums):
            return 0

        res = 1
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                res = max(res, dfs(j) + 1)

        return res

    result = 0
    for k in range(len(nums)):
        result = max(result, dfs(k))

    return result
```

## Memoization (W/Out Backtracking) Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def lengthOfLIS(self, nums: List[int]) -> int:
    memo = defaultdict(int)
    def dfs(i):
        if i in memo:
            return memo[i]

        if i >= len(nums):
            return 0

        memo[i] = 1
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                memo[i] = max(memo[i], dfs(j) + 1)

        return memo[i]

    result = 0
    for k in range(len(nums)):
        result = max(result, dfs(k))

    return result
```

## DP Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def lengthOfLIS(self, nums: List[int]) -> int:
    lis = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                lis[i] = max(lis[i], 1 + lis[j])

    return max(lis)
```