import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap) # O(k)
        
        for i in range(k, len(nums)): # O(n-k)
            if nums[i] > heap[0]:
                heapq.heappop(heap) # O(log k)
                heapq.heappush(heap, nums[i]) # O(log k)
        # O(n-k * (2 log k)) => O(n log k)
        return heap[0]
        
        