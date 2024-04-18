class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheaper = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            cheaper = min(cheaper, prices[i])
            max_profit = max(max_profit, prices[i] - cheaper)

        return max_profit
