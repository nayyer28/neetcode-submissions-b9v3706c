class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp = [False] * (len(nums) - 1)
        dp.append(True)

        n = len(dp) - 2

        while n >= 0:

            for jump in range(nums[n], -1, -1):
                if n + jump >= len(nums) - 1 or dp[n+jump]:
                    dp[n] = True
                    break
            n -= 1
        
        return dp[0]



