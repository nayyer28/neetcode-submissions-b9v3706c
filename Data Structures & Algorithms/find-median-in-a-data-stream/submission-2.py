import heapq
class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)
    # 1 2 3 4 5 6 7 8 9 10
    def findMedian(self) -> float:
        tmp = []
        val = 0
        l = len(self.heap)
        for _ in range(l // 2):
            val = heapq.heappop(self.heap)
            tmp.append(val)

        if l % 2 != 0:
            res = heapq.heappop(self.heap)
            tmp.append(res)
        else:
            val2 = heapq.heappop(self.heap)
            tmp.append(val2)
            res =  (float(val) + float(val2)) / 2
            
        for t in tmp:
                heapq.heappush(self.heap, t)
            
        
        return res
            
        