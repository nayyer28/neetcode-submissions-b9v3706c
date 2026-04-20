class Solution:
    def climbStairs(self, n: int) -> int:
        # tabulation
        k = l = 1
        for _ in range(2, n+1):
            k, l = l, k+l
        
        return l



