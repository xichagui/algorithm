class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        if T == 0:
            return 0

        clips.sort()
        flag = end = 0
        res = 0
        for t in clips:
            if end >= T:
                return res
            
            if t[0] == end:
                if t[1] > end:
                    res += 1
                    end = t[1]
                
            elif t[0] < end:
                if t[1] > end:
                    if end == flag:
                        res += 1
                        end = t[1]

                    elif t[0] <= flag:
                        end = t[1]
                        
                    elif t[0] > flag:
                        flag = end
                        end = t[1]
                        res += 1
                        
            else:
                return -1
        return res if end >= T else -1
# 还能优化, 提前计算每个位置能到达的最远距离, 同时放入数组, 代替排序
