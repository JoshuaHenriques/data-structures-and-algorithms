# 329. Longest Increasing Path in a Matrix
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

*Example 1:*

```
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
```

*Example 2:*

```
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
```

*Example 3:*

```
Input: matrix = [[1]]
Output: 1
```

*Constraints:*

```
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
```

## Top Down Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    longestPath = 1

    def dfs(i, j):
        if i >= len(matrix) or j >= len(matrix[0]):
            return 0

        currMax = 1
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            rdr, cdc = i + dr, j + dc

            if rdr in range(len(matrix)) and cdc in range(len(matrix[0])) and matrix[i][j] < matrix[rdr][cdc]:
                currMax = max(currMax, dfs(rdr, cdc) + 1)

        return currMax

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            longestPath = max(longestPath, dfs(i, j))

    return longestPath
```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    longestPath = 1
    memo = {}

    def dfs(i, j):
        if i >= len(matrix) or j >= len(matrix[0]):
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        currMax = 1
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            rdr, cdc = i + dr, j + dc

            if rdr in range(len(matrix)) and cdc in range(len(matrix[0])) and matrix[i][j] < matrix[rdr][cdc]:
                currMax = max(currMax, dfs(rdr, cdc) + 1)

        memo[(i, j)] = currMax
        return currMax

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            longestPath = max(longestPath, dfs(i, j))
            
    return longestPath
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
