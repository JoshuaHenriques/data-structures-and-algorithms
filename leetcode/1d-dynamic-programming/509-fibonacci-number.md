# 509. Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

*Example 1:*

```
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
```

*Example 2:*

```
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
```

*Example 2:*

```
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
```

*Constraints:*

```
0 <= n <= 30
```

## Top Down Solution (TLE)

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(2^n)$$

$$Space: O(1)$$

### Code
```
def fib(self, n: int) -> int:
    def dfs(n):
        if n == 0:
            return 0

        if n == 1:
            return 1

        return dfs(n - 1) + dfs(n - 2)

    return dfs(n)
```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def fib(self, n: int) -> int:
    memo = { 0: 0, 1: 1 }

    def dfs(n):
        if n in memo:
            return memo[n]

        memo[n] = dfs(n - 1) + dfs(n - 2)
        return memo[n]

    return dfs(n)
```

## Buttom Up DP Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```
def fib(self, n: int) -> int:
    dp = [-1] * (n + 1)
    
    dp[0] = 0        
    if n == 0:
        return dp[0]

    dp[1] = 1
    if n == 1:
        return dp[1]

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```