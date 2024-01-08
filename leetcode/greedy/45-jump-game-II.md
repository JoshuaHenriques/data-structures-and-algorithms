# 45. Jump Game II
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

    0 <= j <= nums[i] and
    i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

*Example 1:*

```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

*Example 2:*

```
Input: nums = [2,3,0,1,4]
Output: 2
```

*Constraints:*

```
1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
```

## Top Down Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(k^n)$$

$$Space: O(n)$$

### Code
```py
def jump(self, nums: List[int]) -> int:
    minJump = float("inf")

    def dfs(i):
        if i >= len(nums) - 1:
            return 0

        jump = float("inf")
        for n in range(nums[i], 0, -1):                 
            jump = min(jump, dfs(n + i) + 1)

        return jump

    return dfs(0)
```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(nk)$$

$$Space: O(n)$$

### Code
```py
def jump(self, nums: List[int]) -> int:
    minJump = float("inf")
    memo = {}

    def dfs(i):
        if i >= len(nums) - 1:
            return 0

        if i in memo:
            return memo[i]

        jump = float("inf")
        for n in range(nums[i], 0, -1):                 
            jump = min(jump, dfs(n + i) + 1)

        memo[i] = jump
        return jump

    return dfs(0)
```

## DP Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(nk)$$

$$Space: O(n)$$

### Code
```py
def jump(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [float("inf") for _ in range(n)]
    dp[0] = 0

    for i in range(n):
        for j in range(1, nums[i] + 1):
            if i + j < n:
                dp[i + j] = min(dp[i] + 1, dp[i + j])

    return dp[n - 1]
```

## Greedy Solution

### Approach
Refer to neetcode video

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```py
def jump(self, nums: List[int]) -> int:
    res = 0
    l = r = 0

    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])

        l = r + 1
        r = farthest
        res += 1

    return res
```
