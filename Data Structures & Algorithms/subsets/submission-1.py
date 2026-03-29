class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        me = nums[0]
        subsets = self.subsets(nums[1:])
        updatedSubsets = []
        for s in subsets:
            updatedSubsets.append(s)
            withMe = s[:]
            withMe.append(me)
            updatedSubsets.append(withMe)
        return updatedSubsets
            
            