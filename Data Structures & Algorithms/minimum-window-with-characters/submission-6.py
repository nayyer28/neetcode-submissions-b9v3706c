class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        tmap = {}
        for c in t:
            tmap[c] = tmap.get(c,0) + 1
        
        needs, has = len(tmap), 0
        l = r = 0
        smap = {}
        mn = float("inf")
        res = ""
        while r < len(s):
            rchar = s[r]
            if rchar in tmap:
                smap[rchar] = smap.get(rchar,0) + 1
                if smap[rchar] == tmap[rchar]:
                    has += 1
            
            while needs == has: # start shortening
                if mn > r - l + 1:
                    mn = r - l + 1
                    res = s[l: r + 1]
                lchar = s[l]

                if lchar in tmap:
                    smap[lchar] -= 1
                    if smap[lchar] < tmap[lchar]:
                        has -= 1
                
                l += 1
            r += 1
        return res
                





