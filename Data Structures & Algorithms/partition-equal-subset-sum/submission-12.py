class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = [True] + ([False] * target)

        for n in nums:
            nxtDp = [False] * (target + 1)
            for j in range(1,target + 1):
                if j >= n:
                    nxtDp[j] = dp[j] or dp[j - n]
                else:
                    nxtDp[j] = dp[j]
            dp = nxtDp
        return dp[-1]
        
        