import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * w for w in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = heapq.heappop(heap) # -6 
            y = heapq.heappop(heap) # - 5
            
            heapq.heappush(heap,x-y) # - 6 + 5 => -1
            
        return -1 * heap[0]

