class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find the slot

        l, r = 0, len(intervals) - 1
        m = 0
        overlap = False
        # O(log N)
        while l <= r:
            m = (l + r) // 2
            if newInterval[0] >= intervals[m][0] and newInterval[0] <= intervals[m][1]:
                intervals[m][1] = max( intervals[m][1], newInterval[1])
                overlap = True
                break
            elif newInterval[0] <  intervals[m][0]:
                r = m - 1
            else:
                l = m + 1
        
        if not overlap: # O(N)
            intervals.insert(l, newInterval)
        
        length = len(intervals)

        res = []
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res


        


       
        