from collections import Counter

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        
        c = None
        for s in A:
            if c is None:
                c = Counter(s)
            else:
                c &= Counter(s)
            
        return list(c.elements())
