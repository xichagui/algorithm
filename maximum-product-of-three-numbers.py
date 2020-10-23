class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a = b = c = -float('inf')
        _a = _b = float('inf')
        
        for num in nums:
            if num > c:
                c = num
            if c > b:
                b, c = c, b
            if b > a:
                a, b = b, a
            
            if num < _b:
                _b = num
            if _b < _a:
                _a, _b = _b, _a
        
        return max(a * b * c, _a * _b * a)
