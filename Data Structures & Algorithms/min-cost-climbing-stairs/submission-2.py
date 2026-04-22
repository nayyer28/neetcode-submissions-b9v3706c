class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # tabulation solution

        res = [0] * (len(cost) + 1)
        i = 0
        
        while i < len(cost) + 1:
            # at me
            prev2 = res[i -2] if i - 2 >= 0 else 0
            prev = res[i -1] if i - 1 >= 0 else 0
            c = cost[i] if i < len(cost) else 0
            res[i] = c + min(prev, prev2)
            i += 1

        return res[-1]
