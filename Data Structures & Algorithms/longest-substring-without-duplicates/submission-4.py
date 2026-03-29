class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  
        hmap = {}
        l, r = 0, 0
        mx_len = 0
        while r < len(s):
            if s[r] in hmap:
                mx_len = max(mx_len, r - l)
                print("mx_len,r,l, s[r]", mx_len, r, l, s[r])
                l = max(hmap[s[r]] + 1,l)
            hmap[s[r]] = r    
            r += 1
        return max(mx_len, r - l)
