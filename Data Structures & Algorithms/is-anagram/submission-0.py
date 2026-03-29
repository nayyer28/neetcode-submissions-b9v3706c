class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}

        for c in s:
            if c in hmap:
                hmap[c] += 1
            else:
                hmap[c] = 1
        
        for c in t:
            if c in hmap:
                hmap[c] -= 1
                if hmap[c] == 0:
                    del hmap[c]
            else:
                return False
        
        if not hmap:
            return True
        return False
            