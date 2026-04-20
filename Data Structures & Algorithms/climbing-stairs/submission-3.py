class Solution:
    def climbStairs(self, n: int) -> int:
        # tabulation
        # O(n) time with O(1) space
        k = l = 1
        for _ in range(2, n+1):
            k, l = l, k+l
        
        return l



