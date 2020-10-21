class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j, m, n = 0, 0, len(name), len(typed)
        
        if m == 0 and n > m:
            return False
        
        while j < n:
            if i < m and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j - 1] == typed[j]:
                j += 1
            else:
                return False
        return i == m
