# 368. Largest Divisible Subset
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

    answer[i] % answer[j] == 0, or
    answer[j] % answer[i] == 0

If there are multiple solutions, return any of them.

*Example 1:*

```
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
```

*Example 2:*

```
Input: nums = [1,2,4,8]
Output: [1,2,4,8]
```

*Constraints:*

* 1 <= nums.length <= 1000
* 1 <= nums[i] <= 2 * 109
* All the integers in nums are unique.

## Naive Solution (TLE)

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```py

```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```py
def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    nums.sort()
    cache = {}

    def dfs(i, prev):
        if i == len(nums):
            return []
        
        if (i, prev) in cache:
            return cache[(i, prev)]

        res = dfs(i + 1, prev)
        if nums[i] % prev == 0:
            tmp = [nums[i]] + dfs(i + 1, nums[i])
            res = tmp if len(tmp) > len(res) else res

        cache[(i, prev)] = res
        return res

    return dfs(0, 1)
```

## DP Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```py

```