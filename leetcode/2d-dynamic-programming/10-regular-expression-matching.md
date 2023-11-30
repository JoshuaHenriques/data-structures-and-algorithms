# 10. Regular Expression Matching
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

*Example 1:*

```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

*Example 2:*

```
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

*Example 3:*

```
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```

*Constraints:*

```
1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
```

## Top Down Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```py
def isMatch(self, s: str, p: str) -> bool:
    def dfs(i, j):
        if j == len(p):
            return  i == len(s)

        first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

        if j + 1 < len(p) and p[j + 1] == '*':
            ans = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
        else:
            ans = first_match and dfs(i + 1, j + 1)

        return ans

    return dfs(0, 0)
```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```py
def isMatch(self, s: str, p: str) -> bool:
    memo = {}
    
    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if j == len(p):
            return  i == len(s)

        first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

        if j + 1 < len(p) and p[j + 1] == '*':
            ans = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
        else:
            ans = first_match and dfs(i + 1, j + 1)

        memo[(i, j)] = ans
        return ans

    return dfs(0, 0)
```

## DP Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```py
def isMatch(self, s: str, p: str) -> bool:
    s, p = ' '+ s, ' '+ p
    lenS, lenP = len(s), len(p)
    dp = [[0]*(lenP) for i in range(lenS)]
    dp[0][0] = 1

    for j in range(1, lenP):
        if p[j] == '*':
            dp[0][j] = dp[0][j-2]

    for i in range(1, lenS):
        for j in range(1, lenP):
            if p[j] in {s[i], '.'}:
                dp[i][j] = dp[i-1][j-1]
            elif p[j] == "*":
                dp[i][j] = dp[i][j-2] or int(dp[i-1][j] and p[j-1] in {s[i], '.'})

    return bool(dp[-1][-1])
```