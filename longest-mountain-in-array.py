class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        
        A.append(10001)
        
        m = 1
        max_m = 0
        
        up = True
        
        for i in range(1, len(A)):
            print(up, m)
            if up:
                if A[i] == A[i - 1]:
                    m = 1
                elif A[i] > A[i - 1]:
                    m += 1
                else:
                    if m >= 2:
                        m += 1
                        up = False
                    else:
                        m = 1
            else:
                if A[i] == A[i - 1]:
                    max_m = max(m, max_m)
                    m = 1
                    up = True
                elif A[i] < A[i - 1]:
                    m += 1
                else:
                    max_m = max(m, max_m)
                    m = 2
                    up = True

        return max_m
                
