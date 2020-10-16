class Solution:
    def totalNQueens(self, n: int) -> int:
        flag = [[0] * n for _ in range(n)]
        res = 0

        def dfs(i, j, flag, num, n):
            if num == n:
                nonlocal res
                res += 1
                return

            if j >= n:
                i += 1
                j = 0

            if i >= n:
                return
            
            for y in range(j, n):
                if flag[i][y] == 0:
                    mark(i, y, flag, n, 1)
                    dfs(i + 1, 0, flag, num + 1, n)
                    mark(i, y, flag, n, -1)

        def mark(x, y, flag, n, point):
            for j in range(n):
                if j != y:
                    flag[x][j] += point

            for i in range(n):
                if i != x:
                    flag[i][y] += point

            temp = x - y
            for i in range(n):
                if 0 <= i - temp < n and i != x:
                    flag[i][i - temp] += point

            temp = x + y
            for j in range(n):
                if 0 <= temp - j < n and j != y:
                    flag[temp - j][j] += point

        dfs(0, 0, flag, 0, n)
        return res
