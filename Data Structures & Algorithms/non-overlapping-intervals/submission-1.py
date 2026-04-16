class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        cnt = 0
        start = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < start:
                cnt += 1
                if intervals[i][1] < start: # decide which to remove - remove that ends later
                    start = intervals[i][1]
            else:
                start = intervals[i][1]
        
        return cnt