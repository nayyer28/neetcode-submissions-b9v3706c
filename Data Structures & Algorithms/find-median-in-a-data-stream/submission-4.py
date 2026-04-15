class MedianFinder:
    # left           <------------>       right
    #  -2 -1                               3 4
    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        if len(self.left) - len(self.right) > 1 or self.right and (- self.left[0]) > self.right[0]:
            pop_left = heapq.heappop(self.left)
            heapq.heappush(self.right, - pop_left)
        
        if len(self.right) - len(self.left) > 1:
            pop_right = heapq.heappop(self.right)
            heapq.heappush(self.left, - pop_right)
            
    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (float(-self.left[0]) + float(self.right[0])) / 2
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]
        
        