class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        
        right = intervals[0][1]
        zoom = 1
        
        for i in range(1, n):
            if intervals[i][0] >= right:
                zoom += 1
                right = intervals[i][1]
        
        return n - zoom

