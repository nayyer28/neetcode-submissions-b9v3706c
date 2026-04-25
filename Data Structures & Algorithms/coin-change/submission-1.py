class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        dp = [float("inf") for _ in range(amount+1)]

        dp[0] = 0
        # amt = 5
        # 2 -> 1 coin
        # 3 -> 1 coin
        # 5 -> 1 + coins or 3 => 2
            # 1 + coins for 2 => 2
        # 2 3
        for i in range(len(dp)):
            for c in coins:
                if c > i:
                    continue
                dp[i] = min(dp[i], 1 + dp[i-c])
        print(dp)
        return dp[-1] if dp[-1] != float("inf") else -1

        # O(t*n) time where n is size of coins array and t is amount with O(t) space