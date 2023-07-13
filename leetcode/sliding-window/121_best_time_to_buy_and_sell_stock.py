# Time limit exceeded 198/212
def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i, len(prices)):
            max_profit = max(max_profit, prices[j] - prices[i])

    return max_profit

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