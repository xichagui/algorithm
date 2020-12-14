from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for _str in strs:
            counts = [0] * 26
            for c in _str:
                counts[ord(c) - ord('a')] += 1
            d[tuple(counts)].append(_str)
        
        return [v for v in d.values()]

