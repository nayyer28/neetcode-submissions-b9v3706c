class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memoization solution
        costs = {}
        # O(n) time with O(n) space - recursion stack + costs array
        def dfs(i:int):
            nonlocal costs
            if i >= len(cost):
                return 0

            if i in costs:
                return costs[i]
            
            # cost of taking me + min (cost of (me + 1), cost of (me + 2))

            costs[i] = cost[i] + min(dfs(i+1), dfs(i+2))

            return costs[i]
        
        return min(dfs(0), dfs(1))
            

