class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # recursive solution
        # start at 0 --> take 1 and take two --> follow path
        # start at 1 --> take 1 and take two --> follow path
        # memoize on whats already calculated
        memo = {}

        def dfs(i:int) -> int:
            nonlocal memo
            if i >= len(cost):
                return 0
            
            if i not in memo:
                memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            
            return memo[i]
        
        return min(dfs(0), dfs(1))