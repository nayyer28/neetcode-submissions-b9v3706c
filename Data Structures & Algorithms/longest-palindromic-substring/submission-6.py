class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # abba -> even
        # aba -> odd
        res = s[0]
        mx = 1
        for center in range(len(s)):
            # odd
            l, r = center - 1, center + 1

            while l > -1 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > mx:
                    mx = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
            
            # even
            l, r = center, center + 1

            while l > -1 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > mx:
                    mx = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
        
        return res
            
        