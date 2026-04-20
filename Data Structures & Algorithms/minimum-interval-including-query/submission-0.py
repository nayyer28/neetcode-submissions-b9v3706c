class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []

        for q in queries:
            mn = float("inf")
            for start, end in intervals:
                if q >= start and q <= end:
                    mn = min(end - start + 1, mn)
            if mn != float("inf"):
                res.append(mn)
            else:
                res.append(-1)
        return res