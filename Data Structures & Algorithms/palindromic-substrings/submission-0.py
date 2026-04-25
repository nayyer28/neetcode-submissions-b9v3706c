class Solution:
    def countSubstrings(self, s: str) -> int:
        # two pointer solution
        # aba
        # abba
        if not s:
            return 0
        # a a a
        cnt = 0
        for center in range(len(s)):
            # odd
            cnt += 1
            
            l, r = center - 1, center + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            
            # even
            l, r = center, center + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
        return cnt
