# 55. Jump Game
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

*Example 1:*

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

*Example 2:*

```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

*Constraints:*

```
1 <= nums.length <= 104
0 <= nums[i] <= 105
```

## Top Down Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n^n)$$

$$Space: O(1)$$

### Code
```py
def canJump(self, nums: List[int]) -> bool:
    def helper(i):
        if i == len(nums) - 1:
            return True

        if i > len(nums) - 1:
            return False

        for n in range(nums[i], -1, -1):
            if n != 0 and i + n < len(nums):
                if helper(i + n):
                    return True

    for n in range(nums[0], -1, -1):
        if helper(n):
            return True

    return False
```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```py
def canJump(self, nums: List[int]) -> bool:
    memo = {}

    def helper(i):
        if i == len(nums) - 1:
            return True

        if i > len(nums) - 1:
            return False

        if i in memo:
            return memo[i]

        for n in range(nums[i], -1, -1):
            if n != 0 and i + n < len(nums):
                if i + n in memo:
                    return memo[i + n]
                memo[i + n] = helper(i + n)
                if memo[i + n]:
                    return True

    for n in range(nums[0], -1, -1):
        if helper(n):
            return True

    return False
```

## DP Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```py
def canJump(self, nums: List[int]) -> bool:
    n = len(nums)
    dp = [False for _ in range(n)]
    dp[0] = True

    for i in range(n):
        if dp[i]:
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = True
                
                if i + j == n - 1:
                    return True

    return dp[n - 1]
```

## Greedy Solution

### Approach
Pass through the array in reverse order and check if the next element is able to reach the last element, if so then update our goal pointer. Keep updating the goal pointer if the next element is able to reach it. By the end of goal is at

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```py
def canJump(self, nums: List[int]) -> bool:
    goal = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return True if goal == 0 else False
```
