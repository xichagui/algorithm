class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
#         len_a = len(A)
#         p, q = 0, len_a - 1
#         while p < q:
#             while A[p] % 2 == 1 and p < q:
#                 p += 1
#             while A[q] % 2 == 0 and p < q:
#                 q -= 1
                
#             A[p], A[q] = A[q], A[p]
        
#         p = 0
#         while p < len_a // 2:
#             A[p] , A[len_a - p - 1] = A[len_a - p - 1], A[p]
#             p += 2
#         return A
        q = 1
        for p in range(0, len(A), 2):
            if A[p] % 2 != 0:
                while q < len(A) and A[q] % 2 == 1 :
                    q += 2
                A[p], A[q] = A[q], A[p]
        
        return A

