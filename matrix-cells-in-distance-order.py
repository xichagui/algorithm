class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        temp_list = [[r0, c0]]
        flag_map = [[False] * C for _ in range(R)]
        flag_map[r0][c0] = True
        
        res = []
        i = 0
        
        while i < len(temp_list):
            res.append(temp_list[i])
            r, c = temp_list[i][0], temp_list[i][1]
            
            if r - 1 >= 0 and not flag_map[r - 1][c]:
                flag_map[r - 1][c] = True
                temp_list.append([r - 1, c])
            
            if c - 1 >= 0 and not flag_map[r][c - 1]:
                flag_map[r][c - 1] = True
                temp_list.append([r, c - 1])
            
            if c + 1 < C and not flag_map[r][c + 1]:
                flag_map[r][c + 1] = 1
                temp_list.append([r, c + 1])
            
            if r + 1 < R and not flag_map[r + 1][c]:
                flag_map[r + 1][c] = 1
                temp_list.append([r + 1, c])
                    
            i += 1
            
        return res
        
