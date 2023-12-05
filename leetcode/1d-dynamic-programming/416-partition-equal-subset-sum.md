# 416. Partition Equal Subset Sum
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

*Example 1:*

```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

*Example 2:*

```
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

*Constraints:*

```
1 <= nums.length <= 200
1 <= nums[i] <= 100
```

## Top Down Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(2^n)$$

$$Space: O(1)$$

### Code
```
def canPartition(self, nums: List[int]) -> bool:
    target = sum(nums) / 2
    
    def dfs(i, curr):
        nonlocal target

        if i >= len(nums):
            return False

        if curr == target:
            return True

        return dfs(i + 1, curr + nums[i]) or dfs(i + 1, curr)

    return dfs(0, 0)
```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n*sum(n))$$

$$Space: O(n*sum(n))$$

### Code
```
def canPartition(self, nums: List[int]) -> bool:
    summation = sum(nums)
    target = summation / 2

    if summation % 2 != 0:
        return False

    memo = {}

    def dfs(i, curr):
        if (i, curr) in memo:
            return memo[(i, curr)]

        if i >= len(nums):
            return False

        if curr == target:
            return True

        memo[(i, curr)] = dfs(i + 1, curr + nums[i]) or dfs(i + 1, curr)

        return memo[(i, curr)]

    return dfs(0, 0)
```

## DP Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n*sum(n))$$

$$Space: O(n*sum(n))$$

### Code
```
def canPartition(self, nums: List[int]) -> bool:
    summation = sum(nums)     
    target = summation / 2

    if summation % 2 != 0:
        return False

    dp = set()
    dp.add(0)

    for i in range(len(nums) - 1, -1, -1):
        nextDP = dp.copy()
        for t in dp:
            if (t + nums[i]) == target:
                return True
            nextDP.add(t + nums[i])

        dp = nextDP

    return False
```