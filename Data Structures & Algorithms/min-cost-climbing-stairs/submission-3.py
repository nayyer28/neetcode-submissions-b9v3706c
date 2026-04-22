class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # tabulation solution

        prev2 = 0
        prev1 = 0
        i = 0
        # O(n) time and O(1) space
        while i < len(cost) + 1:
            c = cost[i] if i < len(cost) else 0
            curr = c + min(prev1, prev2)
            prev2 = prev1 # move by 1
            prev1 = curr # move by 1
            i += 1

        return curr
