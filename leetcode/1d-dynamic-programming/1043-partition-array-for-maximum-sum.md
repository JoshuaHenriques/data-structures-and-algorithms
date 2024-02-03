# 1043. Partition Array for Maximum Sum
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

*Example 1:*

```
Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
```

*Example 2:*

```
Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
```

*Example 3:*

```
Input: arr = [1], k = 1
Output: 1
```

*Constraints:*

* 1 <= arr.length <= 500
* 0 <= arr[i] <= 109
* 1 <= k <= arr.length


## Brute Force Solution (TLE)

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(k^n)$$

$$Space: O(n)$$

### Code
```py
def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
    
    def dfs(i):
        if i >= len(arr):
            return 0

        cur_max = 0
        res = 0
        for j in range(i, min(len(arr), i + k)):
            cur_max = max(cur_max, arr[j])
            window_size = j - i + 1
            res = max(res, dfs(j + 1) + cur_max * window_size)

        return res

    return dfs(0)
```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n*k)$$

$$Space: O(n)$$

### Code
```py
def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
    cache = {}

    def dfs(i):
        if i >= len(arr):
            return 0

        if i in cache:
            return cache[i]

        cur_max = 0
        res = 0
        for j in range(i, min(len(arr), i + k)):
            cur_max = max(cur_max, arr[j])
            window_size = j - i + 1
            res = max(res, dfs(j + 1) + cur_max * window_size)

        cache[i] = res
        return res

    return dfs(0)
```

## Optimized Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```py

```
