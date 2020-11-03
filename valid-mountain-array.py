class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        
        flag = False
        
        if A[0] >= A[1]:
            return False
        
        for i in range(2, len(A)):
            if A[i] == A[i - 1]:
                return False
            
            if not flag:
                if A[i] < A[i - 1]:
                    flag = True
            
            else:
                if A[i] > A[i - 1]:
                    return False
        
        return flag
            
