class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        res = 0
        buy = prices[0] + fee
        
        for price in prices[1::]:
            if price + fee < buy:
                buy = price + fee
            elif price > buy:
                res += price - buy
                buy = price
        return res

