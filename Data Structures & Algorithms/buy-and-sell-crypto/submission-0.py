class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = prices[0], prices[0]
        res = 0
        for i in range(1, len(prices)):
            if l > prices[i]:
                l,r = prices[i], prices[i]
            elif l < prices[i]:
                r = prices[i]
            res = max(0, r - l, res)
        return res