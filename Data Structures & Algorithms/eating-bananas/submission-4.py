class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low, high = 1, max(piles)
        mi = low
        while low <= high:

            k = (low + high) // 2 # rate

            hours = 0

            for p in piles:
                hours += 1 if p < k else math.ceil(float(p) / k)
            
            if hours > h:
                low = k + 1
            else:
                mi = k
                high = k - 1
                
        
        return mi