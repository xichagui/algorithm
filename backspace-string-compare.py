class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        list_s, list_t = [], []
        for s in S:
            if s == '#':
                if list_s:
                    list_s.pop()
            else:
                list_s.append(s)
                
        for t in T:
            if t == '#':
                if list_t:
                    list_t.pop()
            else:
                list_t.append(t)
        
        return list_s == list_t
