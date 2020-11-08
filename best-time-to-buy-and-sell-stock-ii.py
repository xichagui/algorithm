class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_prices = len(prices)
        
        res = 0
        for i in range(len_prices - 1, 0, -1):
            temp = prices[i] - prices[i - 1]
            if temp > 0:
                res += temp
        
        return res

