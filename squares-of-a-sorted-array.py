class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        l1 = []
        l2 = []
        for num in A:
            if num < 0:
                l1.append(num * num)
            else:
                l2.append(num * num)
                
        i = len(l1) - 1 
        j = 0
        
        res = []
        while i >= 0 and j < len(l2):
            if l1[i] < l2[j]:
                res.append(l1[i])
                i -= 1
            else:
                res.append(l2[j])
                j += 1
        
        if i >= 0:
            res.extend(l1[i::-1])
        else:
            res.extend(l2[j:])
        
        return res
