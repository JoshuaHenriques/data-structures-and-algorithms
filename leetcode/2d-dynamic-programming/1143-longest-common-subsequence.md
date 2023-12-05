# 1143. Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

* For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

*Example 1:*

```
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
```

*Example 2:*

```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```

*Example 3:*

```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

*Constraints:*

```
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
```

## Top Down Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(2^(m+n))$$

$$Space: O()$$

### Code
```
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    def dfs(i, j):
        if i >= len(text1) or j >= len(text2):
            return 0

        if text1[i] == text2[j]:
            return dfs(i + 1, j + 1) + 1

        return max(dfs(i + 1, j), dfs(i, j + 1))

    return dfs(0, 0)
```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    memo = [[-1] * len(text2) for _ in range(len(text1))]
    def dfs(i, j):
        if i >= len(text1) or j >= len(text2):
            return 0

        if memo[i][j] != -1:
            return memo[i][j]

        if text1[i] == text2[j]:
            memo[i][j] = dfs(i + 1, j + 1) + 1
            return memo[i][j]

        memo[i][j] = max(dfs(i + 1, j), dfs(i, j + 1))
        return memo[i][j]

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
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    memo = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                memo[i][j] = 1 + memo[i + 1][j + 1]
            else:
                memo[i][j] = max(memo[i + 1][j], memo[i][j + 1])

    return memo[0][0]
```