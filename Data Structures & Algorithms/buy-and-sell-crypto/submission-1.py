class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxSell = 0
        for p in prices:
            g = p - minBuy
            maxSell = max(g, maxSell)
            minBuy = min(p, minBuy)
        return maxSell