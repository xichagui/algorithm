class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        if not A:
            return 0
        
        dict_a_b = {}
        res = 0
        
        for a in A:
            for b in B:
                if a + b in dict_a_b:
                    dict_a_b[a + b] += 1
                else:
                    dict_a_b[a + b] = 1
        
        for c in C:
            for d in D:
                if -(c + d) in dict_a_b:
                    res += dict_a_b[-(c + d)]
        
        return res

