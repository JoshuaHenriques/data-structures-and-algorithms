# 322. Coin Change
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

*Example 1:*

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

*Example 2:*

```
Input: coins = [2], amount = 3
Output: -1
```

*Example 3:*

```
Input: coins = [1], amount = 0
Output: 0
```

*Constraints:*

```
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
```

## Top Down Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(2^n)$$

$$Space: O(1)$$

### Code
```
def coinChange(self, coins: List[int], amount: int) -> int:
    result = float("inf")
    coins = sorted(coins)
    def dfs(i, curr):
        nonlocal result
        if i < 0:
            return 
        if sum(curr) == amount:
            result = min(result, len(curr))
            return 
        elif sum(curr) > amount: 
            return 

        curr.append(coins[i])
        dfs(i, curr.copy())
        curr.pop()
        dfs(i - 1, curr.copy())
    
    dfs(len(coins) - 1, [])
    return -1 if result == float("inf") else result
```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def coinChange(self, coins: List[int], amount: int) -> int:        
    memo = defaultdict(int)

    def dfs(n):
        nonlocal memo
        if memo[n]:
            return memo[n]

        if n == 0:
            return 0

        memo[n] = float("inf")

        for coin in coins:
            if n - coin >= 0:
                memo[n] = min(memo[n], dfs(n-coin) + 1)

        return memo[n]

    result = dfs(amount)
    return result if result != float("inf") else -1
```

## DP Solution (With array)

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def coinChange(self, coins: List[int], amount: int) -> int:        
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])

    return dp[amount] if dp[amount] != amount + 1 else -1
```