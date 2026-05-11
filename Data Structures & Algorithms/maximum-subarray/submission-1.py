class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        mx, mn = float("-inf"), 0
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)-1,-1,-1):
            prefix[i] = prefix[i+1] + nums[i]
            # max possible sum at i = prefix_sum - mn = 4 - 0
            mx = max(mx, prefix[i] - mn)
            mn = min(prefix[i], mn)
        
        return mx

