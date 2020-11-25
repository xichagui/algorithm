class Solution:
    def sortString(self, s: str) -> str:
        fre = [0] * 26
        for c in s:
            fre[ord(c) - 97] += 1
        
        res = ''
        i = 0
        flag = 1
        count = len(s)
        j = 20
        while count:
            while 0 <= i < 26:
                if fre[i]:
                    res += chr(i + 97)
                    fre[i] -= 1
                    count -= 1
                
                i += flag
                
            if i == -1:
                flag = 1
                i = 0
                
            if i == 26:
                flag = -1
                i = 25
        
        return res
        
