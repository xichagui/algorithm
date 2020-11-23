class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 结题思路, 假设有一种最优解. 将所有箭都尽可能往x轴正方向挪.
        # 这样就可以快速得到一种最优解
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        last_right = points[0][1]
        count = 1
        
        for point in points[1:]:
            if point[0] <= last_right:
                continue
            else:
                count += 1
                last_right = point[1]
                
        return count

