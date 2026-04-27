class Solution:
    def numDecodings(self, s: str) -> int:
        # dp - tabulation
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1,len(dp)):
            # one before path
            if int(s[i - 1]) != 0:
                dp[i] += dp[i - 1]
            if s[i-2:i] and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]
        
        return dp[-1]
