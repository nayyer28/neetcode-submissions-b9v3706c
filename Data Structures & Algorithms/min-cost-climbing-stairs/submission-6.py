class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[-2],cost[-1]]

        for i in range(len(cost) - 3, -1, -1):
            dp[1], dp[0] = dp[0], min(dp[1], dp[0]) + cost[i]
        
        return min(dp[0], dp[1])