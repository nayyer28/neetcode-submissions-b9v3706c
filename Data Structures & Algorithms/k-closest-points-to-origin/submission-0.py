import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [((math.sqrt((x)**2 + (y)**2),  i)) for (i, (x,y)) in enumerate(points) ]
        heapq.heapify(dists)
        res = []
        while k > 0:
            i = heapq.heappop(dists)[1]
            res.append(points[i])
            k -= 1
        return res
