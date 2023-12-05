# 494 Target Sum
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.

*Example 1:*

```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
```

*Example 2:*

```
Input: nums = [1], target = 1
Output: 1
```

*Constraints:*

```
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
```

## Top Down Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(2^n)$$

$$Space: O()$$

### Code
```
def findTargetSumWays(self, nums: List[int], target: int) -> int:
    def dfs(i, currSum):
        if i >= len(nums):
            return 1 if currSum == target else 0
        
        return dfs(i + 1, currSum - nums[i]) + dfs(i + 1, currSum + nums[i])

    return dfs(0, 0)
```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n*sum(n))$$

$$Space: O()$$

### Code
```
def findTargetSumWays(self, nums: List[int], target: int) -> int:
    memo = {}

    def dfs(i, currSum):
        if i >= len(nums):
            return 1 if currSum == target else 0

        if (i, currSum) in memo:
            return memo[(i, currSum)]

        memo[(i, currSum)] = dfs(i + 1, currSum - nums[i]) + dfs(i + 1, currSum + nums[i])
        return memo[(i, currSum)]

    return dfs(0, 0)
```

## DP Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
# code
```