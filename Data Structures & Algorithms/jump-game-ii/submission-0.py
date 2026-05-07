class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp = [10000] * len(nums)
        dp[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + nums[i], 0, -1):
                dp[i] = min(dp[i], dp[j] + 1) if j < len(nums) else 1
            
        return dp[0]