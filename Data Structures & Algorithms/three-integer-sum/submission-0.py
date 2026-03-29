class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        i = 0
        res = []
        nums.sort()
        while i < len(nums):

            j, k = i + 1, len(nums) -1

            while j < k:

                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < len(nums) and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while k > -1 and nums[k] == nums[k + 1]:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                    while j < len(nums) and nums[j] == nums[j - 1]:
                        j += 1
                else:
                    k -= 1
                    while k > -1 and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                        i += 1
        return res
                
                
