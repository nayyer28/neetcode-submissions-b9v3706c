class Solution:
    def rob(self, nums: List[int]) -> int:
        # tabulation

        def straight_rob(robs: List[int]):
            rob1, rob2 = 0,0

            for i in range(len(robs)):

                amt = max(rob1, rob2 + robs[i])

                rob2 = rob1
                rob1 = amt
            
            return amt
        
        if len(nums) == 1:
            return nums[0]
        
        return max(straight_rob(nums[1:]), straight_rob(nums[:-1]) )
