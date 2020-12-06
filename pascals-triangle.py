class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res =[[1], [1, 1]]
        if not numRows:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return res
        
        for n in range(2, numRows):
            temp = [1] * (n + 1)
            for i in range(1, (n + 1) // 2 + 1):
                temp[i] = temp[n - i] = res[n - 1][i - 1] + res[n - 1][i]
            res.append(temp)
        
        return res

