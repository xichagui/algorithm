class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    res += 4
                    
                    if i - 1 >= 0:
                        if grid[i - 1][j]:
                            res -= 2

                    if j - 1 >= 0:
                        if grid[i][j - 1]:
                            res -= 2
                
        return res
                
