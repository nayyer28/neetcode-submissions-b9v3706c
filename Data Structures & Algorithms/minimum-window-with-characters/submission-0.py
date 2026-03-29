class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        # OUZODYXAZVYXZABC
        counts1 = {}

        for c in t:
            counts1[c] = counts1.get(c, 0) + 1
        
        need, have = len(counts1.keys()), 0
        counts2 = {}
        l, r = 0, 0
        mil = float("inf")
        shortest = ""
        while r < len(s):
            if have < need:
                counts2[s[r]] = counts2.get(s[r], 0) + 1
                if s[r] in counts1 and counts2[s[r]] == counts1[s[r]]:
                    have += 1
                r += 1
            while need == have:
                if mil > r - l + 1:
                    mil = r - l + 1
                    shortest = s[l:r]
                if s[l] in counts1 and counts2[s[l]] == counts1[s[l]]:
                    have -= 1
                counts2[s[l]] -= 1
                l += 1
            
        return shortest
                




