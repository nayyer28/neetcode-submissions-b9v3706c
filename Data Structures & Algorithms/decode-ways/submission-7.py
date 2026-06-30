class Solution:
    def numDecodings(self, s: str) -> int:
        # 1028
        if s[0] == '0':
            return 0
        dp = [1,1]
        for i in range(1, len(s)):
            tmp = dp[1]

            dp[1] = dp[1] if s[i] != '0' else 0
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[1] += dp[0] if i-2 >=0 else 1
            
            dp[0] = tmp
            # decodings at curr i:
                # decodings at i - 1 if s[i-1] != 0
                # decodings at i - 2 if s[i-1:i+1] is in range
        return dp[1]
        