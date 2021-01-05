class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        
        if not s or len(s) < 3:
            return res
        
        p = 0
        q = 1
        
        while q < len(s):
            if s[q] == s[p]:
                q += 1
            else:
                if q - p >= 3:
                    res.append([p, q - 1])
                p = q
                q += 1
        
        if s[q - 1] == s[p] and  q - p >= 3:
            res.append([p, q - 1])
        
        return res

