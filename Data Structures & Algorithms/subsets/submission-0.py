class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        me = nums[0] # 3
        subs = self.subsets(nums[1:]) # []
        res = []
        for s in subs:
            res.append(s)
            withMe = s[:]
            withMe.append(me)
            res.append(withMe)
        return res
            
            