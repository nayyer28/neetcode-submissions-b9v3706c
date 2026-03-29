class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        heap = []
        l, r = 0, 0
        res = []
        while r <= len(nums):
            if len(heap) >= k:
                while heap[0][1] < l: # max is outside window
                    heapq.heappop(heap)
                res.append(-1 * heap[0][0]) # max
                l += 1
            if r < len(nums):
                heapq.heappush(heap, (-1 * nums[r], r))
            r += 1
        return res
                


                    
