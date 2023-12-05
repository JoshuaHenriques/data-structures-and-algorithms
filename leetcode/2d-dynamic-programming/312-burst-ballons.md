# 312. Burst Balloons
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

*Example 1:*

```
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
```

*Example 2:*

```
Input: nums = [1,5]
Output: 10
```

*Constraints:*

```
n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
```

## Top Down Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def maxCoins(self, nums: List[int]) -> int:
    def dfs(currArr):
        if len(currArr) == 0:
            return 0

        currMax = 0
        for i in range(len(currArr)):
            a = currArr[i-1] if i>0 else 1
            b = currArr[i]
            c = currArr[i+1] if i<len(currArr)-1 else 1

            currMax = max(currMax, a*b*c + dfs(currArr[:i] + currArr[i + 1:]))

        return currMax

    return dfs(nums)
```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def maxCoins(self, nums: List[int]) -> int:
    memo = {}

    def dfs(currArr):
        if len(currArr) == 0:
            return 0

        cache = tuple(currArr)
        if cache in memo:
            return memo[cache]

        currMax = 0
        for i in range(len(currArr)):
            a = currArr[i-1] if i>0 else 1
            b = currArr[i]
            c = currArr[i+1] if i<len(currArr)-1 else 1

            currMax = max(currMax, a*b*c + dfs(currArr[:i] + currArr[i + 1:]))

        memo[cache] = currMax
        return memo[cache]

    return dfs(nums)
```
## Meomoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def maxCoins(self, nums: List[int]) -> int:
    nums = [1] + nums + [1]
    dp = {}

    def dfs(l, r):
        if l > r:
            return 0

        if (l, r) in dp:
            return dp[(l, r)]

        dp[(l, r)] = 0
        for i in range(l, r + 1):
            coins = nums[l - 1] * nums[i] * nums[r + 1]
            coins += dfs(l, i - 1) + dfs(i + 1, r)
            dp[(l, r)] = max(dp[(l, r)], coins)
        
        return dp[(l, r)]

    return dfs(1, len(nums) - 2)
```
