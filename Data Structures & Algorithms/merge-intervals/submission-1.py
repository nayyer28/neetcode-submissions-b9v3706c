class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # O(n log n)
        i = 0
        res = []
        # O(n)
        while i + 1 < len(intervals):
            if intervals[i][1] < intervals[i+1][0]:
                res.append(intervals[i])
            else:
                while i + 1 < len(intervals) and intervals[i][1] >= intervals[i+1][0]:
                    intervals[i+1][0] = min(intervals[i][0], intervals[i+1][0])
                    intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
                    i += 1
                res.append(intervals[i])
            i += 1

        for i in range(i,len(intervals)):
            res.append(intervals[i])

        return res

        # only output list space, so O(1) space
            
            