class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mi, ma = 1, max(piles)
        min_rate = mi
        while mi <= ma:
            rate = (mi + ma) // 2
            
            hours = 0
            for p in piles:
                hours += math.ceil( float(p) / rate)

            if hours > h: # illegitimate hours range
                mi = rate + 1
            else: # legitimate hours range
                min_rate = rate
                ma = rate - 1
        
        return min_rate
            
            