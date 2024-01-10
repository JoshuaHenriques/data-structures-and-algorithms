# 678. Valid Parenthesis String
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


*Example 1:*

```
Input: s = "()"
Output: true
```

*Example 2:*

```
Input: s = "(*)"
Output: true
```

*Example 3:*

```
Input: s = "(*))"
Output: true
```

*Constraints:*

```
1 <= s.length <= 100
s[i] is '(', ')' or '*'.
```

## Top Down Solution (TLE)

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(3^n)$$

$$Space: O(n)$$

### Code
```py
def checkValidString(self, s: str) -> bool:
    n = len(s)

    def dfs(i, left):
        if i == n:
            if left == 0:
                return True
            else:
                return False

        if left < 0:
            return False
        elif s[i] == "(":
            return dfs(i + 1, left + 1)
        elif s[i] == ")":
            return dfs(i + 1, left - 1)
        else:
            return dfs(i + 1, left - 1) or dfs(i + 1, left + 1) or dfs(i + 1, left)

    return dfs(0, 0)
```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n^3)$$

$$Space: O(n)$$

### Code
```py
def checkValidString(self, s: str) -> bool:
    n = len(s)

    memo = {}
    def dfs(i, left):
        if (i, left) in memo:
            return memo[(i, left)]

        if i == n:
            if left == 0:
                return True
            else:
                return False

        if left < 0:
            memo[(i, left)] = False
        elif s[i] == "(":
            memo[(i, left)] = dfs(i + 1, left + 1)
        elif s[i] == ")":
            memo[(i, left)] = dfs(i + 1, left - 1)
        else:
            memo[(i, left)] = dfs(i + 1, left - 1) or dfs(i + 1, left + 1) or dfs(i + 1, left)
        
        return memo[(i, left)]

    return dfs(0, 0)
```

## DP Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n^2)$$

$$Space: O(n^2)$$

### Code
```py
def checkValidString(self, s: str) -> bool:
    n = len(s)

    dp = [[False] * (n + 1) for _ in range(n + 1)]
    dp[n][0] = True

    for i in range(n - 1, -1, -1):
        for j in range(i, -1, -1):
            if s[i] == "*":
                dp[i][j] = (dp[i + 1][j - 1] if j else False) or dp[i + 1][j] or dp[i + 1][j + 1]
            elif s[i] == "(":
                dp[i][j] = dp[i + 1][j + 1]
            else:
                if j: dp[i][j] = dp[i + 1][j - 1]

    return dp[0][0]
```

## Greedy Solution

### Approach
Refer to Neetcode video

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```py
def checkValidString(self, s: str) -> bool:
    leftMin, leftMax = 0, 0

    for c in s:
        if c == "(":
            leftMin, leftMax = leftMin + 1, leftMax + 1
        elif c == ")":
            leftMin, leftMax = leftMin - 1, leftMax -1
        else:
            leftMin, leftMax = leftMin - 1, leftMax + 1

        if leftMax < 0:
            return False
        
        if leftMin < 0:
            leftMin = 0

    return leftMin == 0
```
