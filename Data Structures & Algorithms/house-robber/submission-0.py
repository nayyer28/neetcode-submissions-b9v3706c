class Solution:
    def rob(self, nums: List[int]) -> int:
        # tabulation

        prev1 = 0
        prev2 = 0

        i = 0

        while i < len(nums):

            amt = max(nums[i] + prev2, prev1)

            prev2 = prev1
            prev1 = amt

            i += 1
        
        return amt
