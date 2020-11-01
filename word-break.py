class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict_set = set(wordDict)
        
        longest_word_len = 0
        for length in [len(word) for word in wordDict]:
            longest_word_len = max(longest_word_len, length)
        
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i - 1, -1, -1):
                if i - j > longest_word_len:
                    continue
                    
                if dp[j] and s[j:i] in word_dict_set:
                    dp[i] = True
                    break
        
        return dp[len(s)]

