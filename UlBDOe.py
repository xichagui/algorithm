class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        f = [[0, 0, 0] for _ in range(n)]
        f[0][0] = int(leaves[0] == 'y')
        f[0][1] = f[0][2] = f[1][2] = float('inf')
        
        for i in range(1, n):
            is_red = int(leaves[i] == 'r')
            is_yellow = int(leaves[i] == 'y')
            f[i][0] = f[i - 1][0] + is_yellow
            f[i][1] = min(f[i - 1][0], f[i - 1][1]) + is_red
            if i >= 2:
                f[i][2] = min(f[i - 1][1], f[i - 1][2]) + is_yellow
        
        return f[n - 1][2]
