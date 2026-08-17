class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        # [-1,0,1,2,-1,-4]
        # -4 -1 -1 0 1 2

        i = 0
        res = []
        while i < len(nums):

            j = i + 1
            k = len(nums) - 1

            while j < k:

                s = nums[i] + nums[j] + nums[k]

                if s == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                    
                
                elif s < 0:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        
        return res
                
                    
                
