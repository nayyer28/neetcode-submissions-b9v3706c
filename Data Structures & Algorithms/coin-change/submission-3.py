class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        RANGE = amount + 1
        dp = [float("inf")] * RANGE
        dp[0] = 0

        for amt in range(1,RANGE):
            for c in coins:
                if c <= amt:
                    dp[amt] = min(dp[amt], 1 + dp[amt - c])
        
        return dp[-1] if dp[-1] != float("inf") else -1
            
