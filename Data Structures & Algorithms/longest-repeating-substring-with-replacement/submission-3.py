class Solution:
    def characterReplacement(self, s: str, k: int) -> int:        
        # yxxyxxyy
        # yaxyxbyy
        l = 0
        r = 0
        maxf = 0
        count = {}
        mxl = 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l +=1
            mxl = max(mxl, (r-l+1))
            r += 1
        return mxl




            


