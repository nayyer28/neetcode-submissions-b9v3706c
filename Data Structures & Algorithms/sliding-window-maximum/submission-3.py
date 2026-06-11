import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        heap = []
        l = r = 0
        while r < len(nums):
            
            heapq.heappush(heap, (-nums[r], r))
            if r - l + 1 < k:
                r += 1
                continue
            # size is k
            # pop those beyond left
            while heap[0][1] < l:
                heapq.heappop(heap)
                
            res.append(-heap[0][0])

            l += 1
            r += 1
        return res