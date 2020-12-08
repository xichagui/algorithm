class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        ans = list()
        
        def back_track(index: int):
            if index == len(S):
                return len(ans) >= 3
            
            curr = 0
            for i in range(index, len(S)):
                if i > index and S[index] == '0':
                    break
                curr = curr * 10 + ord(S[i]) - ord('0')
                if curr > 2 ** 31 - 1:
                    break
                
                if len(ans) < 2 or curr == ans[-2] + ans[-1]:
                    ans.append(curr)
                    if back_track(i + 1):
                        return True
                    ans.pop()
                elif len(ans) > 2 and curr > ans[-2] + ans[-1]:
                    break
            
            return False
        
        back_track(0)
        return ans

