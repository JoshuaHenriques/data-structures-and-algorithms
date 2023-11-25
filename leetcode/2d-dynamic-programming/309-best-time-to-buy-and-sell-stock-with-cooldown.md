# 309. Best Time to Buy and Sell Stock with Cooldown
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

    After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

*Example 1:*

```
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
```

*Example 2:*

```
Input: prices = [1]
Output: 0
```

*Constraints:*

```
1 <= prices.length <= 5000
0 <= prices[i] <= 1000
```

## Top Down Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    def dfs(i, j, state, currProfit):
        if j >= len(prices):
            return currProfit

        match state:
            case "buy":
                return max(dfs(i, j + 1, "sell", currProfit - prices[j]), dfs(i, j + 1, "buy", currProfit))
            case "sell":
                return max(dfs(i, j + 1, "cooldown", currProfit + prices[j]), dfs(i, j + 1, "sell", currProfit))
            case "cooldown":
                return dfs(i, j + 1, "buy", currProfit)
    
    for i in range(len(prices)):
        profit = max(profit, dfs(i, i, "buy", 0))

    return profit
```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def maxProfit(self, prices: List[int]) -> int:
    memo = {}

    def dfs(i, buying):
        if i >= len(prices):
            return 0

        if (i, buying) in memo:
            return memo[(i, buying)]

        if buying:
            buy = dfs(i + 1, False) - prices[i]
            not_buy = dfs(i + 1, True)
            memo[(i, buying)] = max(buy, not_buy)
        else:
            sell = dfs(i + 2, True) + prices[i]
            not_sell = dfs(i + 1, False)
            memo[(i, buying)] = max(sell, not_sell)

        return memo[(i, buying)]

    return dfs(0, True)
```

## DP Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def maxProfit(self, prices: List[int]) -> int:
    
    # initialization
    cool_down, sell, hold = 0, 0, -float('inf')
    
    for stock_price_of_Day_i in prices:
        
        prev_cool_down, prev_sell, prev_hold = cool_down, sell, hold
        
        # Max profit of cooldown on Day i comes from either cool down of Day_i-1, or sell out of Day_i-1 and today Day_i is cooling day
        cool_down = max(prev_cool_down, prev_sell)
        
        # Max profit of sell on Day_i comes from hold of Day_i-1 and sell on Day_i
        sell = prev_hold + stock_price_of_Day_i
        
        # Max profit of hold on Day_i comes from either hold of Day_i-1, or cool down on Day_i-1 and buy on Day_i
        hold = max(prev_hold, prev_cool_down - stock_price_of_Day_i)
    
    
    # The action of final trading day must be either sell or cool down
    return max(sell, cool_down)
```