class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # memoization
        TOTAL = sum(nums)
        memo = {}
        def dfs(i: int, p:int):
            if i == len(nums):
                return p == (TOTAL - p)
            
            if (i,p) in memo:
                return memo[(i,p)]
            
            
            memo[(i,p)] =  (dfs(i+1,p+nums[i]) or dfs(i+1, p))

            return memo[(i,p)]
        return dfs(0, 0)



