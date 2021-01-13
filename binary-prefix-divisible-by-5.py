class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        _mod = 0
        for a in A:
            if (_mod := (_mod * 2 + a) % 5) == 0:
                res.append(True)
            else:
                res.append(False)
        
        return res

