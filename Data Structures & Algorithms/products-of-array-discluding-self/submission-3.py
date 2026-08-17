class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        prefix = [1] * len(nums)
        res = [1] * len(nums)
        # left pass
        for i in range(1, len(nums)):
            prefix[i] = prefix[ i - 1 ] * nums[ i - 1 ]
        
        # right pass
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix = suffix * nums[ i + 1 ] if i + 1 < len(nums) else 1
            res[i] = suffix * prefix[i]

        return res
        

        