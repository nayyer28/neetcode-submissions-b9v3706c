class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_straight(robs:List[int]) -> int:
            dp = [0,robs[0]]

            for i in range(1, len(robs)):
                dp[0], dp[1] = dp[1], max(dp[1], robs[i] + dp[0])

            return dp[1]
        
        if len(nums) == 1:
            return nums[0]
        
        return max(rob_straight(nums[1:]), rob_straight(nums[:-1]))