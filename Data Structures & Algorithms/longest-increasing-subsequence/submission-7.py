class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dfs(i: int):
            nonlocal memo
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    memo[i] = max(memo[i], 1 + dfs(j))
                else:
                    dfs(j)
            
            return memo[i]
        
        # why not single call and why max over all indices call?
        # imagine seq 100 50 60 70
        # if you only called from index 0:
        # you will end up with 1 since 100 is greater than all later and index 2 onwwards is never really called
        dfs(0)
        return max(memo)