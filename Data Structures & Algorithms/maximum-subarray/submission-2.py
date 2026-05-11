class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        mx, mn = float("-inf"), 0
        prefix = 0
        for i in range(len(nums)-1,-1,-1):
            prefix = prefix + nums[i]
            # max possible sum at i = prefix_sum - mn = 4 - 0
            mx = max(mx, prefix - mn)
            mn = min(prefix, mn)
        
        return mx

