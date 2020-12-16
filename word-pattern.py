class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if not pattern:
            return False
        
        s_list = s.split(' ')
        if len(pattern) != len(s_list):
            return False
        
        d1 = {}
        pattern_used = set()
        for i in range(len(s_list)):
            if s_list[i] not in d1:
                if pattern[i] not in pattern_used:
                    d1[s_list[i]] = pattern[i]
                    pattern_used.add(pattern[i])
                else:
                    return False
            else:
                if d1[s_list[i]] != pattern[i]:
                    return False
        
        return True
                    
