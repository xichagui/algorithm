class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        word_dict_set = set(wordDict)
        
        @lru_cache(None)
        def dfs(pos):
            if pos == len(s):
                return [[]]
            
            res = []
            
            for i in range(pos + 1, len(s) + 1):
                if s[pos:i] in word_dict_set:
                    temp_res = dfs(i)
                    for word in temp_res:
                        res.append(word.copy() + [s[pos:i]])
            return res
            
        res = dfs(0)
        return [" ".join(word[::-1]) for word in res]

