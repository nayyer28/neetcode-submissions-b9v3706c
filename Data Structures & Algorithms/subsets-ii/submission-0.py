class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # T = O(nlogn) S = O(1) inplace

        res = []
        subset = []

        def dfs(i: int):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # pick
            subset.append(nums[i])
            dfs(i+1)
            #skip
            subset.pop()
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
            dfs(i)
        dfs(0)
        return res
        
