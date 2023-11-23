# 62. Unique Paths
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

*Example 1:*

```
Input: m = 3, n = 7
Output: 28
```

*Example 2:*

```
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

*Constraints:*

```
1 <= m, n <= 100
```

## Top Down Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(2^n)$$

$$Space: O(1)$$

### Code
```
def uniquePaths(self, m: int, n: int) -> int:
    def dfs(row, col):
        if (row, col) == (m - 1, n - 1):
            return 1

        if row == m or col == n:
            return 0

        return dfs(row + 1, col) + dfs(row, col + 1)

    return dfs(0, 0)
```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def uniquePaths(self, m: int, n: int) -> int:
    memo = [[-1] * n for _ in range(m)]

    def dfs(row, col):
        if (row, col) == (m - 1, n - 1):
            return 1

        if row >= m or col >= n:
            return 0

        if memo[row][col] != -1:
            return memo[row][col]

        memo[row][col] = dfs(row + 1, col) + dfs(row, col + 1)
        return memo[row][col]

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
def uniquePaths(self, m: int, n: int) -> int:
    dp = [[-1] * n for _ in range(m)]

    for i in range(m):
        dp[i][n-1] = 1

    for j in range(n):
        dp[m-1][j] = 1

    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            dp[i][j] = dp[i+1][j] + dp[i][j+1]

    return dp[0][0]
```