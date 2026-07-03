class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ms = [0] * len(prices)
        n = len(prices)
        ms[n-1] = prices[n-1]
        for i in range(n -2, -1, -1):
            ms[i] =max(ms[i+1], prices[i])
        mg = 0
        for i in range(0, len(prices) -1, 1):
            g = ms[i+1] - prices[i]
            if g > mg:
                mg = g
        return mg