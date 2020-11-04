class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        flag = False
        res = []
        i = 0
        
        while i < len(intervals):
            
            interval = intervals[i]
            
            if flag:
                if interval[0] <= res[-1][1]:
                    res[-1][1] = max(interval[1], res[-1][1])
                else:
                    res.append(interval)
                i += 1
            else:
            # if res:
                if interval[1] < newInterval[0]:
                    res.append(interval)

                elif newInterval[1] < interval[0]:
                    res.append(newInterval)
                    res.append(interval)
                    flag = True

                else:
                    # 相交
                    res.append([min(interval[0], newInterval[0]), max(interval[1], newInterval[1])])
                    flag = True
                i += 1
                # else:
                    
        if flag == False:
            res.append(newInterval)
            
        return res
        
