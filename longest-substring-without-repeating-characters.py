class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        d = {}
        max_len = 0
        temp = 0
        last_rep = -1
        for i, c in enumerate(s):
            if c in d:
                if d[c] > last_rep:
                    last_rep = d[c]
                    temp = i - last_rep
                else:
                    temp += 1
            else:
                temp += 1
            
            d[c] = i
                
            if temp > max_len:
                max_len = temp
        
        return max_len
