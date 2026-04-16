class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find the slot

        l, r = 0, len(intervals) - 1
        m = 0
        found = False
        while l <= r:
            m = (l + r) // 2
            if newInterval[0] >= intervals[m][0] and newInterval[0] <= intervals[m][1]:
                intervals[m][1] = max( intervals[m][1], newInterval[1])
                found = True
                break
            elif newInterval[0] <  intervals[m][0]:
                r = m - 1
            else:
                l = m + 1
        
        if not found:
            intervals.insert(l, newInterval)
            start = l
        else:
            start = m
        
        l = len(intervals)

        while start + 1 < l and intervals[start][1] >= intervals[start+1][0]:
            intervals[start][1] = max(intervals[start][1], intervals[start+1][1])
            intervals.pop(start+1)
            l = len(intervals)

        return intervals


        


       
        