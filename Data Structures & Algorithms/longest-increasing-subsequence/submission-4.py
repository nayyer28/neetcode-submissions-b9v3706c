class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # memoization - top down
        memo = {}
        def dfs(i : int, cmp: int):
            if i == len(nums):
                return 0
            
            if (i, cmp) in memo:
                return memo[(i,cmp)]
            
            # dont take ith value in seq
            memo[(i,cmp)] = dfs(i+1, cmp)

            # take ith value in seq
            if nums[i] > cmp:
                memo[(i,cmp)] = max(memo[(i,cmp)] , dfs(i+1, nums[i]) + 1)
            
            return memo[(i,cmp)]

        return dfs(0, float("-inf"))