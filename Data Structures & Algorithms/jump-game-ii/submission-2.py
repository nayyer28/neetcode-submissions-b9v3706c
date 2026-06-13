class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[-1] = 0
        
        for i in range(len(nums)-2, -1, -1):
            for j in range(nums[i], 0, -1):
                dp[i] = min(dp[i], 1 + dp[i+j]) if i+j < len(nums) else 1
        return dp[0]