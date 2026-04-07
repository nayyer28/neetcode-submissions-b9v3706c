import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap) # O(n)
        while k > 0: # O(k log n)
            res = heapq.heappop(heap)
            k -= 1
        return - res
        # O(k log n)
        
        