class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        dp = [[False] * len(s) for _ in range(len(s))]
        mx = float("-inf")
        ix = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if mx < (j - i + 1):
                        mx = j - i + 1
                        ix = i
        return s[ix:ix+mx]

        
        