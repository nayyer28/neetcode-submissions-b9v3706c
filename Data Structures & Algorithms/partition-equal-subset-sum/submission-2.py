class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # memoization
        memo = {}
        def dfs(i: int, p:int):
            if i == len(nums):
                return p == (sum(nums) - p)
            
            if (i,p) in memo:
                return memo[(i,p)]
            
            
            memo[(i,p)] =  (dfs(i+1,p+nums[i]) or dfs(i+1, p))

            return memo[(i,p)]
        return dfs(0, 0)



