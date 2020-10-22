class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        num = len(strs)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    if j >= zeros and k >= ones:
                        dp[j][k] = max(dp[j][k], dp[j - zeros][k - ones] + 1)
        return dp[m][n]
