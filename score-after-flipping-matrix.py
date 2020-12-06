class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        
        n = len(A)
        m = len(A[0])

        res = n
        
        for j in range(1, m):
            count_1 = 0
            for i in range(n):
                if not A[i][j] ^ A[i][0]:
                    count_1 += 1
            res = res * 2 + max(count_1, n - count_1)
        
        return res

