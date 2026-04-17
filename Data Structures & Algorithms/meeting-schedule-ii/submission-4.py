"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        timestamps = []
        for i in intervals:
            start = i.start
            end = i.end
            timestamps.append((True, start))
            timestamps.append((False, end))
        timestamps.sort(key=lambda x : (x[1], x[0]))

        cnt = 0
        mx = 0

        for isStart, _ in timestamps:
            if isStart:
                cnt += 1
                mx = max(mx, cnt)
            else:
                cnt -= 1
        
        return mx