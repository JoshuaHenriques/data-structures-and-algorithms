# 115. Distinct Subsequences
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.d

*Example 1:*

```
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
```

*Example 2:*

```
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
```

*Constraints:*

```
1 <= s.length, t.length <= 1000
s and t consist of English letters.
```

## Top Down Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def numDistinct(self, s: str, t: str) -> int:
    def dfs(i, j):
        if j >= len(t):
            return 1
            
        if i >= len(s):
            return 0

        if s[i] == t[j]:
            return dfs(i + 1, j + 1) + dfs(i + 1, j)
        else:
            return dfs(i + 1, j)  

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
def numDistinct(self, s: str, t: str) -> int:
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if j >= len(t):
            return 1
            
        if i >= len(s):
            return 0

        if s[i] == t[j]:
            memo[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            return memo[(i, j)]
        
        memo[(i, j)] = dfs(i + 1, j)  
        return memo[(i, j)]
        
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