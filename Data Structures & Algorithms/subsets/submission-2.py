class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i:int, subset:List[int]):
            if i == len(nums):
                res.append(subset.copy())
                return
            # add self
            subset.append(nums[i])
            # call dfs
            dfs(i+1, subset)
            # remove self
            subset.pop()
            # call dfs
            dfs(i+1,subset)
        dfs(0, [])

        return res
            