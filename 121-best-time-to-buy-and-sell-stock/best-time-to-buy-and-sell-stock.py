class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_for = [0] * n
        maximum = prices[-1]
        max_profit = 0

        for i in range(n - 2, -1, -1):
            maximum = max(prices[i], maximum)
            max_for[i] = maximum

        for i, price in enumerate(prices):
            max_profit = max(max_profit, max_for[i] - price)

        return max_profit