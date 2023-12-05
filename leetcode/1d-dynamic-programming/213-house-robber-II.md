# 213. House Robber II
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

*Example 1:*

```
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
```

*Example 2:*

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

*Example 3:*

```
Input: nums = [1,2,3]
Output: 3
```

*Constraints:*

```
1 <= nums.length <= 100
0 <= nums[i] <= 1000
```

## Naive Solution (Time Limit Exceeded)

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(2^n)$$

$$Space: O(1)$$

### Code
```
def rob(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    def dfs(numsArr, i):
            if i >= len(numsArr):
                return 0
            
            return max(dfs(numsArr, i + 1), numsArr[i] + dfs(numsArr, i + 2))

    return max(dfs(nums[1:], 0), dfs(nums[:-1], 0))
```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def rob(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    memo = {}
    def dfs(numsArr, i):
        if i >= len(numsArr):
            return 0

        if i not in memo:
            memo[i] = max(dfs(numsArr, i + 1), numsArr[i] + dfs(numsArr, i + 2))

        return memo[i]
    
    a = dfs(nums[:-1], 0)
    memo = {}
    b = dfs(nums[1:], 0)
    return max(a, b)
```

## DP Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```
def rob(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    def dfs(nums):
            rob1, rob2 = 0, 0

            for n in nums:
                newRob = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = newRob

            return rob2
        
    return max(dfs(nums[1:]), dfs(nums[:-1]))
```