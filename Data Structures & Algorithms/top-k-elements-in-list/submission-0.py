import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        heap = []
        for num, c in count.items():
            heapq.heappush(heap, (c, num))
            if len(heap) > k:
                heapq.heappop(heap)
        out = []
        for c, n in heap:
            out.append(n)
        return out