class Solution:
    def numDecodings(self, s: str) -> int:
        # 1028
        # 1111
        # 012345
        if s[0] == '0':
            return 0
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(dp)):
            dp[i] = dp[i-1] if s[i] != '0' else 0
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2] if i-2 >=0 else 1
            # decodings at curr i:
                # decodings at i - 1 if s[i-1] != 0
                # decodings at i - 2 if s[i-1:i+1] is in range
        return dp[-1]
        