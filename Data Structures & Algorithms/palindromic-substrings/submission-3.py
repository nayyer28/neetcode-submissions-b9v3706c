class Solution:
    def countSubstrings(self, s: str) -> int:
        # abba -> even
        # aba -> odd
        # abc
        cnt = 0
        for center in range(len(s)):
            # odd
            l = r = center
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                cnt += 1
            
            # even
            l, r = center, center + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                cnt += 1
        
        return cnt