# 121. Best TIme to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

*Example 1:*

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

*Example 2:*

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

*Constraints:*

```
1 <= prices.length <= 105
0 <= prices[i] <= 104
```

## Naive Solution (Time Limit Exceeded)

### Approach
Using two for loops, calculate the profit for each day with every other day to keep track of the max profit

### Complexity
$$Time: O(n^2)$$

$$Space: O(1)$$

### Code
```
def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i, len(prices)):
            max_profit = max(max_profit, prices[j] - prices[i])

    return max_profite
```

## Optimized Solution

### Approach
Using the sliding window algorithm we make two pointers, i starts at 0 and j is always i + 1, if prices[i] is ever greater than prices[j] we slide the "window" by 1, i = j and j += 1. If not then we calculate the profit and replace the max profit if it's higher and we just increment the j pointer to increase the size of the "window"

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```
def maxProfit2(self, prices: List[int]) -> int:
    max_profit = 0

    i, j = 0, 1
    while j < len(prices):
        if prices[i] >= prices[j]:
            i = j
        else:
            max_profit = max(max_profit, prices[j]-prices[i])
        j += 1     

    return max_profit
```