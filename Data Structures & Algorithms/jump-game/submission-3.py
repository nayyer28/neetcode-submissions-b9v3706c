class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp = [False] * (len(nums) - 1)
        dp.append(True)

        for n in range(len(nums) - 2, -1, -1):

            for jump in range(nums[n], -1, -1):
                if n + jump >= len(nums) - 1 or dp[n+jump]:
                    dp[n] = True
                    break
        
        return dp[0]



